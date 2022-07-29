# api key
KEY = '6faa1c397d5b4b59a792ced2a27b6f44'
import re
from math import ceil
from newsapi.newsapi_client import NewsApiClient
#found today's date
# today and tomorrow
# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta
  
  
# Get today's date
presentday = datetime.now() # or presentday = datetime.today()
  
# Get Yesterday
yesterday = presentday - timedelta(1) 
  
# strftime() is to format date according to
# the need by converting them to string
y = yesterday.strftime('%d-%m-%Y')
t= presentday.strftime('%d-%m-%Y')


# Init
newsapi = NewsApiClient(api_key=KEY)

def headlines_from_subject_or_category(q='bitcoin', language= 'en', category= 'business', country='us',part=1):
    # category is very important
    top_headlines = newsapi.get_top_headlines(q='bitcoin', category= category,language= 'en', country=country )
    print(y,t)
    return news_process(news=top_headlines, part=part)


def news_from_subject_or_category(q='bitcoin', language= 'en', from_date = y, to_date = t, part=1):
    # return a string explaining the news
    news = newsapi.get_everything(q=q.lower(), language= 'en', from_param = from_date, to = to_date, sort_by = 'relevancy')
    return news_process(news=news, part=part)


def just_news(language= 'en',  part=1):
    # return a string explaining the news
    news = newsapi.get_top_headlines(language= 'en')
    return news_process(news=news, part= part)


def news_process(news,part):
    if news['status'] != 'ok':
        return ''
    count = news['totalResults']
    articles = news['articles']
    required_fields = ['source', 'title', 'description']
    articles = [{key:value for key, value in article.items() if key in required_fields} for article in articles] # keeping only keys we need
    strings_for_nexws = []
    sentences = [f"In the {str(article['source']['name']).replace('(','').replace(')','')}, this article named '{article['title']}'.\nIt talks about {article['description']} " for article in articles ]
    return '\n\n'.join(map(str, sentences[:min(5, ceil(len(sentences)*part ))]))