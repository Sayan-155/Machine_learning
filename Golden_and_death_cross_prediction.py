import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("TVSMOTOR.csv" , parse_dates= ['Date'] , index_col= 'Date')

# calculate the 30 day and 6 day SMA
sma_6 = df['Close'].rolling(window= 6).mean()
sma_30 = df['Close'].rolling(window= 30).mean()

# define a function to detect crossover signals
def detect_crossover(data , short_window= 10 , long_window= 40):
    df['sma_short'] = df['Close'].rolling(window= short_window).mean() # sma_10
    df['sma_long'] = df['Close'].rolling(window= long_window).mean() # sma_30
    
    # initialize list to store crossover event dates
    golden_cross_dates = []
    death_cross_dates = []
    
    # loop through the data
    for i in range(1 , len(data)):
        
        # extract the previous and current SMA values.
        prev_short = data['sma_short'].iloc[i-1]
        prev_long = data['sma_long'].iloc[i-1]
        
        curr_short = data['sma_short'].iloc[i]
        curr_long = data['sma_long'].iloc[i]
        
        # ensure that all values are numeric (not NAN)
        if pd.notna(prev_short) and pd.notna(prev_long) and pd.notna(curr_short) and pd.notna(curr_long):
            # detect the golden cross
            if prev_short < prev_long and curr_short > curr_long:
                golden_cross_dates.append(data.index[i])
            
            # detect death cross
            elif prev_short > prev_long and curr_short < curr_long:
                death_cross_dates.append(data.index[i])
                
    # return the lists
    return golden_cross_dates , death_cross_dates
    
golden_cross, death_cross = detect_crossover(df)

# plot the data
plt.figure(figsize= (16,8))
plt.plot(df.index , df['Close'] , label= 'close price' , color= 'yellow' , alpha= 0.5)

# plot the crossovers
plt.plot(df.index , df['sma_short'] , label= 'SMA short' , color= 'brown' , alpha= 0.5)
plt.plot(df.index , df['sma_long'] , label= 'SMA short' , color= 'blue' , alpha= 0.5)

# add crossover markers
plt.scatter(golden_cross , df.loc[golden_cross , 'Close'] , marker= '^' , color= 'green' , label= 'Golden cross')
plt.scatter(golden_cross , df.loc[death_cross , 'Close'] , marker= 'v' , color= 'red' , label= 'Death cross')

plt.title('Golden & Death crosses')
plt.xlabel('Date')
plt.ylabel('Close price')
plt.legend()
plt.grid(True)
plt.show()

