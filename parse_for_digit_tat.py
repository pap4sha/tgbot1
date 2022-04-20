import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


def get_first_news():
    # Назначение юзер агента и юрл адреса Comnews для парсинга
    headers = {'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Mobile Safari/537.36'}
    url = 'https://digital.tatarstan.ru/index.htm/news/tape'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all(class_="col-xs-12 col-sm-9")

    news_dict = {}

    for article in articles_cards:
        article_date = article.find('div', class_="date").text.strip()
        article_title = article.find("div", class_="list_title").text.strip()
        article_desc = article.find('div', class_="list_text").text.strip()
        article_url = f'https://digital.tatarstan.ru{article.find("a").get("href")}'

        article_id = article_url.split("/")
        article_id = article_id[4]


        print(f"{article_date} | {article_title} | {article_desc} | {article_url}")


