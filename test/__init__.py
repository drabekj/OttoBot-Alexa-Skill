import requests

from app.models import Stock


ticker_list = ['TSLA','FB','SNAP','SQ', 'UAL']
changes = Stock.get_change_batch(ticker_list)

for item in changes:
    print(str(item) + ",")
