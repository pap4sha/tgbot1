, import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


def get_first_news():
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Mobile Safari/537.36'}
    url = 'https://www.comnews.ru/news'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all(class_="field-content")

    news_dict = {}

    for article in articles_cards:
        article_date = article.find('div', class_="date").text.strip()
        article_title = article.find("div", class_="title").text.strip()
        article_desc = article.find('div', class_="body").text.strip()
        article_url = f'https://www.comnews.ru{article.find("a").get("href")}'

        article_id = article_url.split("/")
        article_id = article_id[4]


        #print(f"{article_date} | {article_title} | {article_desc} | {article_url}")

        news_dict[article_id] = {
            "article_date": article_date,
            "article_title": article_title,
            "article_url": article_url,
            "article_des": article_desc
        }

    with open('news_dict.json', 'w') as file:
       json.dump(news_dict, file, indent=4, ensure_ascii=False)

def check_news_update():
#файл куда сохранятются спарсенные данные по новостям
    with open('news_dict.json') as file:
        new_dict = json.load(file)


#создание переменной для парсинга и назначение контейнера в котором лежат новости
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all(class_="field-content")

    fresh_news = {}

#поиск уникального кода новости
    for article in articles_cards:
        article_url = f'https://www.comnews.ru{article.find("a").get("href")}'
        article_id = article_url.split("/")
        article_id = article_id[4]

#если код новости есть продолжить, иначе занести данные по новости в файл news_dict.json
        if article_id in new_dict:
            continue
        else:
            article_date = article.find('div', class_="date").text.strip()  #вытаскивание даты из сайта
            article_title = article.find("div", class_="title").text.strip()    #вытаскивание заголовка из сайта
            article_desc = article.find('div', class_="body").text.strip()  #вытаскивание превью новости
            article_url = f'https://www.comnews.ru{article.find("a").get("href")}'  #вытскивание поолного юрл новости

#Запись новости в файл news_dict.json
            new_dict[article_id] = {
                "article_date": article_date,
                "article_title": article_title,
                "article_url": article_url,
                "article_des": article_desc
            }

            fresh_news[article_id] = {
                "article_date": article_date,
                "article_title": article_title,
                "article_url": article_url,
                "article_des": article_desc
            }

    with open('news_dict.json', 'w') as file:
       json.dump(new_dict, file, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    # get_first_news()
    print(check_news_update())


if __name__ == "__main__":
    main()