import streamlit as st
import yfinance as yf

import requests
from bs4 import BeautifulSoup

import requests_cache

SESSION = requests_cache.CachedSession("yfinance.cache")
SESSION.headers["User-agent"] = "stockpredictor/0.1.0"

@st.cache_data
def load_data(ticker, START, TODAY):
    data = yf.download(ticker, session=SESSION, start=START, end=TODAY)
    data.reset_index(inplace=True)
    return data

def get_news(ticker):
    data = yf.Ticker(ticker)
    links = [item["link"] for item in data.news]
    
    # Scapping News
    try:
        news = []
        for link in links:
            response = requests.get(link).content
            p_tags = BeautifulSoup(response, "html.parser").find_all("p")

            contents = [content.get_text() for content in p_tags if len(content.get_text()) > 100]

            x = " ".join(contents)
            if x != "":
                news.append(x)

    except:
        return "Something wrong, try again later :smile:"

    return news

