from urllib.request import urlopen

import feedparser
from bs4 import BeautifulSoup as bs, NavigableString, Comment

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
            logger.exception(f"Can't get link to article at index:{index}", e)
            return None

        return link

    def get_article_body(self, index):
        """ Get the text body of article at {index}
        :return: str or None if failed
        """
        url = self.get_article_link(index)
        logger.debug(f"article link: {url}")

        soup = bs(urlopen(url), "html.parser")

        article_text = soup.find(id="articleText")
        if article_text is None:
            article_text = soup.find(id="articlebody")

        content = ""
        for paragraph in article_text:
            if type(paragraph) == NavigableString \
                    or type(paragraph) == Comment \
                    or paragraph.text == "" \
                    or paragraph.text == "\n":
                continue

            for p in paragraph:
                if type(p) == NavigableString \
                        or type(p) == Comment \
                        or p.text == "" \
                        or p.text == "\n":
                    continue

                content += self._unify_spaces(p.text) + "\n"

        # cut content to 7500 characters
        if len(content) > 7500:
            logger.warning(f"The card content is too long ({len(content)}) and will be cut.")
            content = content[:7500] + "..."

        return content

    def _unify_spaces(self, text):
        """Replace multiple spaces with one."""
        return ' '.join(text.split())
