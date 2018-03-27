from urllib.request import urlopen

import feedparser
from bs4 import BeautifulSoup as bs

from app import logger


class FeedReader(object):
    def __init__(self, ticker):
        self.data = feedparser.parse(
            f'http://articlefeeds.nasdaq.com/nasdaq/symbols?symbol={ticker}')

    def get_articles_titles(self, limit=3):
        """ Get list of article headings.
        :param limit: limit the number of titles received (max 10)
        :return: [string]
        """
        if limit > 10:
            logger.error("Can't read that many titles, set limit to max 10.")

        articles = []
        for index, article in enumerate(self.data['entries']):
            if index >= limit:
                break
            articles.append(article['title'])

        return articles

    def get_article_link(self, index):
        """ Get link to the article at {index}.
        :return: str link or None if failed to find link
        """
        try:
            article = self.data['entries'][index]
            link = article['feedburner_origlink']
        except Exception as e:
            logger.exception(f"Couldn't get link to article at index:{index}", e)
            return None

        return link

    def get_article_body(self, index):
        """ Get the text body of article at {index}
        :return: str or None if failed
        """
        url = self.get_article_link(index)
        soup = bs(urlopen(url), "html.parser")

        article_body = soup.find(id="articlebody")

        # kill all script and style elements
        for script in article_body(["script", "style"]):
            script.extract()

        # get text
        text = article_body.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in
                  line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text
        