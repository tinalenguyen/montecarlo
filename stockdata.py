from datetime import date, timedelta
from pytrends.request import TrendReq
import plotly.express as px
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt

def getcompanytrends():
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Microsoft Stocks"]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    historicaldf = pytrends.interest_over_time()
    fig = px.line(historicaldf, y="Microsoft Stocks", title="Monte Carlo Simulation") 
    fig.update_layout(title_x=0.5, font_color="Black", font_family="Sans Serif")
    fig.show()
    print(historicaldf)


def getCurrentPrice(company):
    stock = yf.Ticker(company)
    currentprice = stock.info['currentPrice']
    return currentprice

def getURL(company):
    URL=f"https://www.{company}.com"
    stock = yf.Ticker(company)
    info = stock.info
    website = info.get("website", "N/A")
    website=website[12:]
    return website

def getLongname():
    return stock.info['longName']

def getSummary():
    return stock.info['longBusinessSummary']

def getStaff():
    return stock.info['companyOfficers']

def getAddress():
    addr=stock.info['address1']+", "+stock.info['city']+", "+stock.info['state']+" "+stock.info['zip']
    return addr

def info(company):
    global stock
    stock=yf.Ticker(company)
    print(stock.info)
