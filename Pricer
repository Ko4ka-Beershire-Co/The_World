# Environment
import numpy as np
import pandas as pd

# TEMP for testing from .csv
data = pd.read_csv('Data.csv')
price = data.Price


def pricing(price_array, tau):
    # Tell-a-trend
    global Up
    MA_price = price_array.rolling(tau).mean()
    MA_price.fillna(price_array, inplace=True)

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


print(pricing(price, 3))
