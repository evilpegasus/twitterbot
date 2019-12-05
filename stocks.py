import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def stock_info(ticker):
    today = date.today()
    data = yf.download(ticker, period="1d")
    open_price = data["Open"]
    close_price = data['Close']
    change = close_price - open_price
    return open_price[0], close_price[0], change[0]
