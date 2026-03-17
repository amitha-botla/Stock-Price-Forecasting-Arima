# Stock Price Forecasting with ARIMA

Time series analysis and forecasting of equity prices using ARIMA modelling on real financial market data.

## Overview
This project applies ARIMA (AutoRegressive Integrated Moving Average) modelling to historical stock price data to generate short-term price forecasts. Real market data is pulled directly via the yfinance API.

## Features
- Retrieves real historical stock price data (AAPL, 2020–2024)
- Tests for stationarity using the Augmented Dickey-Fuller (ADF) test
- Fits an ARIMA model to closing price time series
- Generates and visualises a 30-day price forecast

## Tech Stack
- Python
- pandas
- statsmodels
- yfinance
- matplotlib
- streamlit

## Results
The ARIMA(5,1,0) model was fitted on AAPL closing prices from January 2020 to January 2024. The 30-day forecast is plotted against historical prices, showing the model captures the general trend direction.
ARIMA forecasts on non-stationary financial data tend to revert to a mean, a known limitation addressed in more advanced models like GARCH or LSTM

## How to Run
1. Clone the repo
2. Install dependencies:
```
   pip install yfinance pandas matplotlib statsmodels
```
3. Open and run `stock_price_forecasting.ipynb`
