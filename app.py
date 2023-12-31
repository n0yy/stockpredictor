import streamlit as st
from datetime import date

from src.load_data import load_data, get_news
from src.plot_data import plot_stock
from src.model import StockForecast
from src.database import Database

st.set_page_config(page_title="Tuyul Modern")

START = "2017-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
STOCKS = ('GOOG', 'AAPL', 'MSFT', 'AMZN', 'BABA', 'AAL', 'IBM')

st.title("ReksaDanang :chart_with_upwards_trend: :chart_with_downwards_trend:")

selected_stock = st.selectbox("Choose Stock", STOCKS)
n_years = st.slider("Select Period", min_value=0.5, max_value=3.0)
period = int(n_years * 365)

submit = st.button("Submit :rocket:", type="primary")


if submit:
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

    # SECTION: SENTIMENT ANALYSIS
    st.subheader("SENTIMENT ANALYSIS :sunglasses:")
    # Get News
    db = Database(selected_stock)
    with st.spinner("Wait a minute.."):
        news = get_news(selected_stock)
        db.createTable()
        db.insertTable(news)
        news_db = db.get_data()
        st.write(news_db)



