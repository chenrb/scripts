# -*- coding: utf-8 -*-
"""
蓝鲸模拟登录获取bk_token
使用V6
"""
import requests

bk_paas_host = ""
login_csrftoken_name = "bklogin_csrftoken"


def login(username, password):
    login_url = "{}/login/?c_url=/%3Flogin_type%3Dbk".format(bk_paas_host)
    session = requests.Session()
    resp = session.get(login_url, verify=False)
    csrftoken = resp.cookies.get(login_csrftoken_name)
    login_data = {
        "csrfmiddlewaretoken": csrftoken,
        "username": username, "password": password
    }
    login_resp = session.post(login_url, data=login_data, headers={"Referer": login_url})
    bk_token = login_resp.cookies.get("bk_token")
    return bk_token
