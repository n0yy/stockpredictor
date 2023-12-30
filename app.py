import streamlit as st
from datetime import date

from src.load_data import load_data, get_news
from src.plot_data import plot_stock
from src.model import StockForecast

st.set_page_config(page_title="Tuyul Modern")

START = "2017-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
STOCKS = ('Saham', 'ANTM.JK', 'BBCA.JK', 'GOOG', 'AAPL', 'MSFT', 'GME')

st.title("Tuyul Era 5.0 :sunglasses:")

selected_stock = st.selectbox("Pilih Saham", STOCKS)
n_years = st.slider("Berapa Tahun untuk memprediksi", min_value=1, max_value=3)
period = n_years * 365

if selected_stock != 'Saham':
    data_load_state = st.text("Tunggu bwanngggg!!")
    stock_data = load_data(selected_stock, START, TODAY)
    data_load_state.text("Done!")

    # Show Table Stock
    st.subheader(f"Table Saham | {selected_stock}")
    st.write(stock_data.tail())

    plot_stock(stock_data, selected_stock)

    # Data Selecting
    data_train = stock_data[["Date", "Close"]]
    data_train = data_train.rename(columns={"Date": "ds", "Close": "y"})

    # Model
    model = StockForecast()
    forecast = model.predict(data_train, period)
    model.show_forecast(forecast)

    # Get News
    news = get_news(selected_stock)
    st.write(news)


