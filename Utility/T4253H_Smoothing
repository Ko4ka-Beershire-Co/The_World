# Environment
import numpy
import pandas as pd

# TEMP for testing
vector = [1, 2, 3, 4, 5, 6, 7, 7.7, 6, 8, 9, 5, 8, 12]


def running_median(array, window):
    s = pd.Series(array)
    output = s.rolling(window).median()
    return output


def t4253h_smoothing(array):
    s = pd.Series(array)
    i = s.rolling(4).median()
    i.fillna(s, inplace=True)

    s = i
    i = i.rolling(2).median()
    i.fillna(s, inplace=True)

    s = i
    i = i.rolling(5).median()
    i.fillna(s, inplace=True)

    s = i
    i = i.rolling(3).median()
    i.fillna(s, inplace=True)
    return i


def MA(array, tau, fill = False):
    MA_price = array.rolling(tau).sum()
    if fill:
        MA_price.fillna(array, inplace=True)
    return MA_price
    
    
print(t4253h_smoothing(vector))
