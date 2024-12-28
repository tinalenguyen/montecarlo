import plotly.express as px
import numpy as np
import pandas as pd

from datetime import date, timedelta, datetime
from pytrends.request import TrendReq

import yfinance as yf

class MontecarloAlgo():
    def __init__(
            self,
            *,
            company: str | None = None,
    ):
        self._company = company

        self._data = yf.download(self._company, period="max")

        self._standard_deviation: float | None
        self._cumulative_mean: float | None

        self._dataframe = self.get_cumulative_data()
        
    @property
    def standard_deviation(self) -> float:
        return self._standard_deviation
    
    @property
    def cumulative_mean(self) -> float:
        return self._cumulative_mean

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe
    

    
# def montecarlo(company):
#     global data

#     data = yf.download(company, period="max")

    def get_cumulative_data(self) -> pd.DataFrame:
        print(self._data)   
        prices = self._data['Close']

        log_returns = np.log(prices / prices.shift(1)).dropna()
        mean_log_return = log_returns.mean()
        std_log_return = log_returns.std()
        delta_t = 1/252  

        num_simulations = 2000

        avgprices = []
        dates = []
        for x in range(num_simulations):
            price_series = [prices.iloc[-1]]
            y=0
            daytracker = 0
            while y < 365:
                currdate =date.today() + timedelta(days=y)
                if (currdate.weekday()<5):
                    epsilon = np.random.normal()
                    price = price_series[-1] * np.exp((mean_log_return - 0.5 * std_log_return**2) * delta_t + std_log_return * epsilon * np.sqrt(delta_t))
                    price_series.append(price)
                    if x==0:
                        avgprices.append(price)
                        dates.append(currdate)
            
                    else:
                        newavg = (avgprices[daytracker] + price)/2
                        avgprices[daytracker]=newavg
                daytracker+=1
            y+=1
    
        mean = (sum(avgprices))/len(avgprices)

        total=0
        for i in range(len(avgprices)):
            diff = avgprices[i]-mean
            total+= (diff*diff)
        standev=total/len(avgprices)

        simdata= {
            "Date": dates,
            "Averaged Stock Price": avgprices
        }

        global simulation_df
        simulation_df = pd.DataFrame(simdata)

        return simulation_df

# def getCumMean():
#     return mean

# def getStanDev():
#     return standev
# input format 2099-01-01, example if 2023 was submitted, year=2024-01-01
    def montecarlotest(self, year):
    # CALCULATE PREDICTED
        startdate =datetime.strptime(year, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
        
        pricehist =  self._data.loc[self._data.index < startdate, 'Adj Close']

        log_returns = np.log(pricehist / pricehist.shift(1)).dropna()
        mean_log_return = log_returns.mean()
        std_log_return = log_returns.std()
        delta_t = 1/252  

        num_simulations = 2000
        num_days = 252  
    
        avgprices = []
        dates = []

        for x in range(num_simulations):
            price_series = [pricehist.iloc[-1]]
            y=0
            daytracker = 0
            while y < 365:
                currdate  = startdate + timedelta(days=y)
                if (currdate.weekday()<5):
                    epsilon = np.random.normal()
                    price = price_series[-1] * np.exp((mean_log_return - 0.5 * std_log_return**2) * delta_t + std_log_return * epsilon * np.sqrt(delta_t))
                    price_series.append(price)
                    if x==0:
                        avgprices.append(price)
                        dates.append(currdate)

                    else:
                        newavg = (avgprices[daytracker] + price)/2
                        avgprices[daytracker]=newavg
                    daytracker+=1
                y+=1
        
        
        simdata= {
            "Date": dates,
            "Averaged Stock Price": avgprices
        }
        predicteddf = pd.DataFrame(simdata)

        predicteddf['Date'] = pd.to_datetime(predicteddf['Date'])
        # CALCULATE ACTUAL
        enddate =  startdate + timedelta(days=365)
        
        mask = ((self._data.index >= startdate) & (self._data.index < enddate))
        actualprice =  self._data.loc[mask, 'Adj Close']

        actualdf =  pd.DataFrame(actualprice)
        sumactual =actualdf['Adj Close'].sum()
        print(sumactual)
        sumpredict = predicteddf['Averaged Stock Price'].sum()
        print(sumpredict)

        accuracy = abs((sumactual-sumpredict)) / sumactual
        accuracy *= 100
        print(accuracy)

        

        global concatdf
        concatdf = predicteddf.merge(actualdf, left_on='Date', right_index=True)

        formattedtitle = "Monte Carlo Simulation (" + year[:4] + ")" 

        fig = px.line(concatdf, x='Date', y=['Averaged Stock Price', 'Adj Close'], title=formattedtitle) 
        fig.update_layout(title_x=0.5, font_color="Black", font_family="Sans Serif")

        fig.show()

        plotly_jinja_data=fig.to_html(full_html=False)
        
        return plotly_jinja_data

