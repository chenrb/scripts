"""
蓝鲸发送邮件
"""
import base64
import json
import traceback
import urllib.parse

import requests

bk_app_code = ""
bk_app_secret = ""
bk_username = ""
receiver__username = ""
bk_paas_host = ""
send_mail_url = "/api/c/compapi/cmsi/send_mail/"

MONTH_REPORT = """
        <div style="position: relative;">
            <div class="bk-logs-basic">
                <ul>
                    <li><span class="bk-basic-title">项目名: </span> <span class="bk-basic-value">DDDD</span></li>
                </ul>
            </div>
            <div class="demo-line"></div>
            <div class="bk-basic-img">
                <img src="cid:line1" width="900" height="900"/>
            </div>
            <div class="demo-line"></div>
            <h6>当前使用情况(): </h6>
            <div class="bk-basic-img">
                <img src="data:image/png;base64,${resource_radar_content}" width="900" height="700"/>
            </div>
        </div>
        <style type="text/css">
            .bk-logs-basic {
                margin: 20px 10px 10px;
                min-height: 100px;
            }
            .bk-logs-basic ul .clearfix:after {
                display: block;
                clear: both;
                content: "";
                font-size: 0;
                visibility: hidden;
            }
            .bk-logs-basic li {
                padding-left: 5px;
                padding-right: 5px;
                float: left;
                width: 32%;
                font-size: 14px;
                line-height: 27px;
                color: #63656e;
                word-break: break-all;
                word-wrap: break-word;
                list-style-type: none;
                /*overflow: hidden;*/
                /*white-space: pre-wrap;*/
                /*text-overflow: ellipsis;*/
            }
            .bk-logs-basic li .bk-basic-title {
                display: inline-block;
                min-width: 70px;
                font-weight: bold;
            }
            .bk-logs-basic li .bk-basic-value {
                padding-left: 10px;
            }
            .bk-logs-basic li li:first-child {
                width: 100%;
            }
            .bk-basic-img {
                margin: 10px;
                text-align: center;
            }
            .demo-line {  
                padding: 0 20px 0;  
                margin: 20px 0;  
                line-height: 1px;  
                border-left: 190px solid #ddd;  
                border-right: 190px solid #ddd;  
                text-align: center;  
            }
            .fl-table {
                margin: 20px;
                border-radius: 5px;
                font-size: 12px;
                border: none;
                border-collapse: collapse;
                max-width: 100%;
                white-space: nowrap;
                word-break: keep-all;
            }

            .fl-table th {
                text-align: left;
                font-size: 20px;
            }

            .fl-table tr {
                display: table-row;
                vertical-align: inherit;
                border-color: inherit;
            }

            .fl-table tr:hover td {
                background: #00d1b2;
                color: #F8F8F8;
            }

            .fl-table td, .fl-table th {
                border-style: none;
                border-top: 1px solid #dbdbdb;
                border-left: 1px solid #dbdbdb;
                border-bottom: 3px solid #dbdbdb;
                border-right: 1px solid #dbdbdb;
                padding: .5em .55em;
                font-size: 15px;
            }

            .fl-table td {
                border-style: none;
                font-size: 15px;
                vertical-align: center;
                border-bottom: 1px solid #dbdbdb;
                border-left: 1px solid #dbdbdb;
                border-right: 1px solid #dbdbdb;
                height: 30px;
            }

            .fl-table tr:nth-child(even) {
                background: #F8F8F8;
            }
        </style>
        """

filename = "2023-02-16_2_line.jpeg"


def make_file_content(file_path):
    image_content = ""
    try:
        with open(file_path, "rb") as f:
            image_content = base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        print("month_resource_report error: {}".format(traceback.format_exc()))
    return image_content


csvname = "20230301-20230331.csv"


def send_email():
    url = urllib.parse.urljoin(bk_paas_host, send_mail_url)
    params = {
        "bk_app_code": bk_app_code,
        "bk_app_secret": bk_app_secret,
        "bk_username": bk_username,
        "receiver__username": receiver__username,
        "title": "测试",
        "content": MONTH_REPORT,
        "attachments": [
            {
                "filename": "2023-02-16_2_line.jpeg",
                "content": make_file_content(file_path=filename),
                "type": "jpeg",
                "disposition": "inline",
                "content_id": "line1"
            },
            {
                "filename": "蓝鲸主机资源_20230301-20230331.csv",
                "content": make_file_content(file_path=csvname)
            }
        ]
    }

    response = requests.post(url=url, data=json.dumps(params), verify=False)
    print(response.json())


if __name__ == '__main__':
    send_email()
