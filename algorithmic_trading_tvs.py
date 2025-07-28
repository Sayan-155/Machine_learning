# Description -> This program uses the moving target cross over to determine whe buy and sell stocks

# import libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Read the data
df = pd.read_csv("TVSMOTOR.csv")

# make simple moving average
SMA_10 = pd.DataFrame()
SMA_10['Adj Close'] = df['Adj Close'].rolling(window= 5).mean()

SMA_50 = pd.DataFrame()
SMA_50['Adj Close'] = df['Adj Close'].rolling(window= 20).mean()

# visualize the data
plt.figure(figsize= (12,8))
plt.plot(df['Adj Close'] , label= 'TVSMotor')
plt.plot(SMA_10['Adj Close'] , label= 'SMA10')
plt.plot(SMA_50['Adj Close'] , label= 'SMA50')
plt.title('Apple Share price')
plt.legend(loc= 'upper left')
plt.show()

# make a new dataframe
data = pd.DataFrame()
data['TVSMotor'] = df['Adj Close']
data['SMA10'] = SMA_10['Adj Close']
data['SMA50'] = SMA_50['Adj Close']

# make algorithmic prediction
def buy_sell(data):
    signal_price_buy = []
    signal_price_sell = []
    flag = -1
    
    for i in range(0 , len(data)):
        if data['SMA10'][i] > data['SMA50'][i] :
            if flag != 1:
                signal_price_buy.append(data['AAPL'][i])
                signal_price_sell.append(np.nan)
                flag = 1   
            else :
                signal_price_buy.append(np.nan)
                signal_price_sell.append(np.nan)
                
        elif data['SMA10'][i] < data['SMA50'][i] :
            if flag !=0 :
                signal_price_buy.append(np.nan)      
                signal_price_sell.append(data['TVSMotor'][i])
                flag = 0
            else:
                signal_price_buy.append(np.nan)
                signal_price_sell.append(np.nan)
                
        else:
            signal_price_buy.append(np.nan)
            signal_price_sell.append(np.nan)
                
    return (signal_price_buy , signal_price_sell)
                
# store buy and sell data into a variable
buy_sel = buy_sell(data)
data['Buy_Signal_price'] =buy_sel[0]
data['Sell_Signal_price'] =buy_sel[1]
