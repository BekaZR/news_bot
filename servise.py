# last_news = datetime.strptime(last_date, "%Y-%m-%d")
from datetime import datetime


def get_valid_datetime(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    return date


def custom_crono(default_time_publishid, time_sleep_value):
    time_ = datetime.today().time().hour
    if time_ < default_time_publishid:
        default_time_publishid = default_time_publishid - time_
        time_sleep_value = default_time_publishid * 60 * 60
        return time_sleep_value
    elif time_ > default_time_publishid:
        default_time_publishid = (time_sleep_value - time_) + default_time_publishid
        time_sleep_value = default_time_publishid * 60 * 60
        return time_sleep_value