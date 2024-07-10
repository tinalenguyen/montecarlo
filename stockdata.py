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
    # historicaldf = trends.get_historical_interest('apple', year_start=2020, month_start=10, day_start=1, hour_start=0, year_end=2021, month_end=10, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
    kw_list = ["Microsoft Stocks"]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    #visualise
    #plot a timeseries chart
    # historicaldf.plot(figsize=(20, 12))
    historicaldf = pytrends.interest_over_time()
    #plot seperate graphs, using theprovided keywords
    # historicaldf.plot(subplots=True, figsize=(20, 12))
    fig = px.line(historicaldf, y="Microsoft Stocks", title="Monte Carlo Simulation") 
    fig.update_layout(title_x=0.5, font_color="Black", font_family="Sans Serif")
    fig.show()
    print(historicaldf)
    # return trends

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


# print(getURL("AAPL"))

# webscraping mumbo jumbo
    # company+=" company"
    # searchurl = f""
    # search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={company}&limit=1&namespace=0&format=json"
    # search_response = requests.get(search_url).json()
    # page_title = search_response[1][0]
    # print(search_response)

    # images_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={company}&prop=images&format=json"
    # images_response = requests.get(images_url).json()
    # page_id = list(images_response['query']['pages'].keys())[0]
    # images = images_response['query']['pages'][page_id].get('images', [])

    # # Step 3: Get image URLs
    # image_titles = "|".join([img['title'] for img in images])
    # image_info_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={image_titles}&prop=imageinfo&iiprop=url&format=json"
    # image_info_response = requests.get(image_info_url).json()
    # print(image_info_response)
    # # image_urls = []
    # # for page in image_info_response['query']['pages'].values():
    # #     if 'imageinfo' in page:
    # #         image_urls.append(page['imageinfo'][0]['url'])

