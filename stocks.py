import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def stock_info(ticker):
    today = date.today()
    data = yf.download(ticker, start=today, end=today, group_by="ticker")
    open_price = data["Open"]
    close_price = data['Close']
    change = close_price - open_price
    return change

print(stock_info("TSLA"))