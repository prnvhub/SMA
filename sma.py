import pandas as pd
import datetime as dt

# Load the file
data=pd.read_excel('RELIANCE.xlsx')

# Formatting the date and removing time.
data['Date']=pd.to_datetime(data['Date'], format='%Y-%m-%d').dt.date

# SMA of 10 Days
data['SMA(Open) 10D']=data['Open'].rolling(10, min_periods=5).mean()
data['SMA(High) 10D']=data['High'].rolling(10, min_periods=9).mean()
data['SMA(Low) 10D']=data['Low'].rolling(10, min_periods=9).mean()
data['SMA(Close) 10D']=data['Close'].rolling(10, min_periods=9).mean()
data['SMA(Adj Close) 10D']=data['Adj Close'].rolling(10, min_periods=9).mean()
data['SMA(Volume) 10D']=data['Volume'].rolling(10, min_periods=9).mean()
data.tail()
# print(data)
data.to_excel('RELIANCE.xlsx', index=False)