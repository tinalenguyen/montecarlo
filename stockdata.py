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

