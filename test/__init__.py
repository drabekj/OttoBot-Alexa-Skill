import requests

from app.models import Stock


ticker_list = ['TSLA','FB','SNAP','SQ', 'UAL']
ticker = "AAPL"

data = Stock.get_stats(ticker)
print(data)
