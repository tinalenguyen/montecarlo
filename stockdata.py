from datetime import date, timedelta
from pytrends.request import TrendReq
import yfinance as yf
import numpy as np
import pandas as pd
import requests
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

