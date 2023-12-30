import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly

class StockForecast:
    def __init__(self):
        self.model = Prophet()
        
    def predict(self, df_train, period):
        self.model.fit(df_train)

        future = self.model.make_future_dataframe(period)
        forecast = self.model.predict(future)

        return forecast
    
    # Show Forecast
    def show_forecast(self, forecast):
        st.subheader("Stock's Forecast")
        st.write(forecast.tail())

        st.subheader(f"Stock's Forecast Plot")
        fig1 = plot_plotly(self.model, forecast)
        st.plotly_chart(fig1)

        st.write("Stock's Component")
        fig2 = self.model.plot_components(forecast)
        st.write(fig2)