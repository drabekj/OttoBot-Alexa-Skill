import feedparser


class FeedReader(object):
    def __init__(self, ticker):
        self.data = feedparser.parse(
            f'http://articlefeeds.nasdaq.com/nasdaq/symbols?symbol={ticker}')

    def get_articles_titles(self, limit=3):
        """ Get list of article headings.
        :param limit: limit the number of titles received
        :return: [string]
        """
        articles = []
        for index, article in enumerate(self.data['entries']):
            if index >= limit:
                break
            articles.append(article['title'])

        return articles
