from datetime import date, timedelta
from pytrends.request import TrendReq
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getStockData(company):
    data = yf.download(company, period="max")
    return data

def getcompanytrends(company):
    trends = TrendReq()

def getCurrentPrice(company):
    stock = yf.Ticker(company)
    currentprice = stock.info['currentPrice']
    formatted_number = f"${currentprice:.2f}"
    return formatted_number



