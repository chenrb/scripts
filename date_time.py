# -*- coding: utf-8 -*-
import datetime


def get_last_day_of_prev_month(fmt_need=True, fmt="%Y-%m-%d"):
    today = datetime.date.today()
    first_day_of_this_month = datetime.date(today.year, today.month, 1)
    last_day_of_prev_month = first_day_of_this_month - datetime.timedelta(days=1)
    if not fmt_need:
        return last_day_of_prev_month
    return last_day_of_prev_month.strftime(fmt)


def get_first_day_of_prev_month(fmt_need=True, fmt="%Y-%m-%d"):
    last_day_of_prev_month = get_last_day_of_prev_month(fmt_need=False)
    first_day_of_prev_month = datetime.date(last_day_of_prev_month.year, last_day_of_prev_month.month, 1)
    if not fmt_need:
        return first_day_of_prev_month
    return first_day_of_prev_month.strftime(fmt)


if __name__ == '__main__':
    first_day_of_prev_month_str = get_first_day_of_prev_month()
    last_day_of_prev_month_str = get_last_day_of_prev_month()
    print("上个月第一天是：", first_day_of_prev_month_str)
    print("上个月最后一天是：", last_day_of_prev_month_str)