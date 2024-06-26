from datetime import date, timedelta
import numpy as np
import pandas as pd
from datetime import date, timedelta
from pytrends.request import TrendReq
import yfinance as yf



def montecarlo(company):

    data = yf.download(company, period="max")
    prices = data['Adj Close']

    log_returns = np.log(prices / prices.shift(1)).dropna()
    mean_log_return = log_returns.mean()
    std_log_return = log_returns.std()
    delta_t = 1/252  

    num_simulations = 2000
    num_days = 252  

    avgprices = []
    dates = []

    for x in range(num_simulations):
        price_series = [prices.iloc[-1]]
        for y in range(num_days):
            epsilon = np.random.normal()
            price = price_series[-1] * np.exp((mean_log_return - 0.5 * std_log_return**2) * delta_t + std_log_return * epsilon * np.sqrt(delta_t))
            price_series.append(price)
            if x==0:
                avgprices.append(price)
                dates.append(date.today() + timedelta(days=y))
            else:
                newavg = (avgprices[y] + price)/2
                avgprices[y]=newavg
            
    simdata= {
        "Date": dates,
        "Averaged Stock Price": avgprices
    }

    simulation_df = pd.DataFrame(simdata)

    return simulation_df
# montecarlo()

