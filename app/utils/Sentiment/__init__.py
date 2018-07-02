from app.utils.YahooFinanceParser import YahooFinanceParser


class Analyst(object):
    def __init__(self, ticker):
        self.ticker = ticker

    def recommendation(self):
        """
        Analyst's recommendation his stock. What should the  investor do?
        :return: float number on scale 1-5 (eg. 2.3 means recommendation to hold inclined to buying)
            Strong-buy: 1
            Buy: 2
            Hold: 3
            Underperform: 4
            Sell: 5
        """
        recommendation = YahooFinanceParser(self.ticker).get_analyst_recommendation()
        print(f"The recommendation is {recommendation}")
