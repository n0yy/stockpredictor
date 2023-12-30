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
    news = []
    for link in links:
        response = requests.get(link).content
        p_tags = BeautifulSoup(response, "html.parser").find_all("p")
        
        contents = []
        for text in p_tags:
            contents.append(text.get_text())
        
        x = " ".join(contents)
        news.append(x)
        
    return news

