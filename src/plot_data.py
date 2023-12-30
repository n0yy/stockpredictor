from plotly import graph_objects as gobs
import streamlit as st

# Plotting Chart Stock
def plot_stock(data, name_stock):
    fig = gobs.Figure()
    fig.add_trace(gobs.Line(x=data["Date"], y=data["Open"], name="Open"))
    fig.add_trace(gobs.Line(x=data["Date"], y=data["Close"], name="Close"))
    fig.layout.update(title_text=f"Time Series Data | {name_stock}", xaxis_rangeslider_visible=True)

    st.plotly_chart(fig)
