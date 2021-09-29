from flask import Flask
from urllib.request import urlopen

from bs4 import BeautifulSoup as soup

#setting news_url to from where we are fetching news
news_url = "https://news.google.com/news/rss"

app = Flask(__name__)


def get_news_from_google():
    # using urlopen function and giving him the news_url and storing it into client
    client = urlopen(news_url)
    page = client.read()

    #now we are using read function and reading the client data and setting it into page
    client.close()

    souped = soup(page, "xml")
    #now we are using beautifulsoup and giving page and setting it into xml

    news_list = souped.findAll("item")
    #now geeting item form souped variable with help of findall func and store in varibale

    result = []
    #now creating blank list

    for news in news_list:
        #looping through the news_list

        data = {}
        # blank dictionary

        data['title'] = news.title.text
        #storing title of news getiing from looping and storing in dictionary

        data['date'] = news.pubDate.text
        #same as above

        result.append(data)
        #now adding data into list using apend method

    return result
    #returnig the list


@app.route('/')
def index():
    news = get_news_from_google()
    return {'result': news}


if __name__ == '__main__':
    app.run(debug=True)