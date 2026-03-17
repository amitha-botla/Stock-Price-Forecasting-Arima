import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

st.title("Stock Price Forecasting with ARIMA")

# Sidebar inputs
ticker = st.sidebar.text_input("Stock Ticker", value="AAPL")
start = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-01-01"))
forecast_days = st.sidebar.slider("Forecast Days", 10, 60, 30)

# Load data
df = yf.download(ticker, start=start, end=end)["Close"]

st.subheader(f"{ticker} Historical Price")
st.line_chart(df)

# ADF Test
result = adfuller(df)
st.subheader("Stationarity Test (ADF)")
st.write(f"ADF Statistic: {result[0]:.4f}")
st.write(f"p-value: {result[1]:.4f}")

# ARIMA Model
model = ARIMA(df, order=(5,1,0))
fitted = model.fit()

# Forecast
forecast = fitted.forecast(steps=forecast_days)
forecast_index = pd.date_range(start=df.index[-1], periods=forecast_days+1, freq='B')[1:]
forecast_series = pd.Series(forecast.values, index=forecast_index)

# Plot
st.subheader(f"{forecast_days}-Day Price Forecast")
fig, ax = plt.subplots(figsize=(12,5))
ax.plot(df, label="Historical")
ax.plot(forecast_series, label="Forecast", color="red")
ax.legend()
st.pyplot(fig)