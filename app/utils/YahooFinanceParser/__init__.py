from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import re
from json import loads


class YahooFinanceParser(object):
    def __init__(self, ticker):
        self.ticker = ticker

        url = f'https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}'
        self.soup = bs(urlopen(url), "html.parser")

    def get_analyst_recommendation(self):
        """
        Analyst's recommendation of the stock.
        :return: float number on scale 1-5 (eg. 2.3 means recommendation to hold inclined to buying)
            Strong-buy: 1
            Buy: 2
            Hold: 3
            Underperform: 4
            Sell: 5
        """
        # load json from contents
        data = self.soup.find("script", text=re.compile("root.App.main")).text
        data = loads(re.search("root.App.main\s+=\s+(\{.*\})", data).group(1))

        # get recommendationMean from json
        recommendation_mean = data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"][
            "financialData"]["recommendationMean"]["raw"]
        return recommendation_mean
