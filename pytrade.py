import sys
import pandas
import yfinance as yf
from datetime import date

# The general idea of the script would be to:
# 1. Gather a list of stock tickers you're interested in
# 2. Calculate the Sharpe ratio for each of these stocks
#    a. Note: Given stock performance over the last 10 years
# 3. Balance them with an amount of risk that the user provides

# ref: https://towardsdatascience.com/calculating-sharpe-ratio-with-python-755dcb346805

todayDate = date.today().isoformat()
startDate = '2010-1-1'

stockSymbol = 'SPY'
stockSymbols = sys.argv[1:]

stockData = yf.Ticker(stockSymbol)

# Need to create a for loop to create dataframes for each tickerSymbol

stockDataFrame = stockData.history(period='1y', start=startDate, end=todayDate)
pandas.set_option("display.max_rows", None, "display.max_columns", None)

print(stockDataFrame['Close'])

# Calculating Normalized Return by dividing close price by yesterday's close price
stockDataFrame['Normalized Return'] = stockDataFrame['Close'].div(stockDataFrame['Close'].shift(1))


# print(tickerDf.iloc[0])

# print(tickerDf['Close'])
# for stock_df in tickerSymbols:
# tickerDf['Normalized Return'] = tickerDf['Close'][1] / tickerDf.iloc[0]['Close'][1]

print(stockDataFrame['Normalized Return'])