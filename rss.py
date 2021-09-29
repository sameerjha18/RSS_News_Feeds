from flask import Flask
from urllib.request import urlopen

from bs4 import BeautifulSoup as soup

news_url = "https://news.google.com/news/rss"

app = Flask(__name__)


def get_news_from_google():
    client = urlopen(news_url)
    page = client.read()
    client.close()
    souped = soup(page, "xml")
    news_list = souped.findAll("item")
    result = []
    for news in news_list:
        data = {}
        data['title'] = news.title.text
        data['date'] = news.pubDate.text
        result.append(data)
    return result


@app.route('/')
def index():
    news = get_news_from_google()
    return {'result': news}


if __name__ == '__main__':
    app.run(debug=True)