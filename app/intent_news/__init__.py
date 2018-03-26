from app import AlexaRequest, ResponseBuilder
from app.utils import Ticker2Name
from app.utils.FeedReader import FeedReader
from static import strings


def handle_news(request):
    """:type request AlexaRequest"""
    ticker = request.get_slot_value('stockTicker')
    company = Ticker2Name.ticker_to_name(ticker)

    headings = FeedReader(ticker).get_articles_titles()
    message_content = ". ".join(headings)

    message = strings.INTENT_NEWS_ABOUT_COMPANY_INTRO.format(company) \
              + message_content
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(message=reprompt_message)