# Environment
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date


def get_data(ticker, interval, start_date="2019-1-1", end_date='today'):
    # Today handling (obvious IMHO)
    if end_date == "today":
        today = date.today()
        end_date = str(today)
    if OSError:   # FFS there is always an error
        print("Error: Dude something's wrong with your end_date")
    # actual parcing
    data = yf.download(ticker, start_date, end_date, interval)['Adj Close']
    df_data = pd.DataFrame(data)   # this one is "just in case"
    return df_data['Adj Close']  # data is a pd.Dataframe


def pricing(price_array, tau):
    # Tell-a-trend
    MA_price = price_array.rolling(tau).mean()   # Rolling mean of tau window
    MA_price.fillna(price_array, inplace=True)   # Rolling mean(right) removes some data, so we replace it
    
    # algorithm for pricing (readme.md for more info)
    if (price_array[len(price_array) - 1]) - (MA_price[len(MA_price) - 1]) > np.std(price_array):
        Trend = True
        if (price_array[len(price_array) - 1]) - (MA_price[len(MA_price) - 1]) > 0:
            Up = True
        if (price_array[len(price_array) - 1]) - (MA_price[len(MA_price) - 1]) < 0:
            Down = True
    if (price_array[len(price_array) - 1]) - (MA_price[len(MA_price) - 1]) < np.std(price_array):
        Trend = False

    # Fair_Price
    if not Trend:
        fair_price = MA_price[len(price_array) - 1]
    if Trend:
        if Up:
            fair_price = MA_price[len(price_array) - 1] + np.std(price_array)
        if Down:
            fair_price = MA_price[len(price_array) - 1] - np.std(price_array)

    return fair_price


def runner(ticker, mult_long=0.333, mult_med=0.333, mult_short=0.333, start_date="2019-1-1",
           end_date='today'):  # the weights are taken as arguments
    # Long_int
    data_long = get_data(ticker, '1mo', start_date, end_date)
    price_long = pricing(data_long, 3)   # manual tau
    # Med_int
    data_med = get_data(ticker, '1wk', start_date, end_date)
    price_med = pricing(data_med, 5)   # manual tau
    # Short_int
    data_short = get_data(ticker, '1d', start_date, end_date)
    price_short = pricing(data_short, 7)   # manual tau
    # Final weights
    end_price = mult_long * int(price_long) + mult_med * int(price_med) + mult_short * int(price_short)
    # Test

    return end_price


####################################
######### THE MAGIC BUTTON #########
####################################

print(runner('AMZN'))  # enter the ticker to launch the thing
