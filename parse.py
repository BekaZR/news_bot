from calendar import month
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
import requests
from servise import get_valid_datetime

link = "https://www.python.org/blogs/"

last_date = {"time": datetime.today()}


def get_response():
    response = requests.get(link).text
    return response


def get_all_post():
    soup = BeautifulSoup(get_response(), "lxml")
    all_post = soup.find('ul', class_="list-recent-posts menu")
    post_list = all_post.find_all("li")
    return post_list


def get_last_news():
    date_list = []
    url_list = []
    for post in get_all_post():
        date = post.find("time").get("datetime")
        # if get_valid_datetime(date) > get_valid_datetime(last_date.get('time')):
        if get_valid_datetime(date) > last_date.get('time'):
            date_list.append(date)
            url_data = post.find("h3", class_ = "event-title")
            url = url_data.find("a").get('href')
            url_list.append(url)

    if date_list:
        last_date['time'] = max(date_list)
        
    print(last_date)
    if url_list: 
        return url_list
    return None
