from app import AlexaRequest, ResponseBuilder
from app.utils import Ticker2Name
from app.utils.FeedReader import FeedReader
from static import strings

news_count = 3

def handle_news(request):
    """:type request AlexaRequest"""

    if request.dialog_state() == "STARTED":
        return _handle_dialog_read_titles(request)
    if request.dialog_state() == "IN_PROGRESS":
        if request.get_slot_value('articleNo') is None:
            if request.get_intent_confirmation_status() == "CONFIRMED":
                # Ask user which article he wants details about
                return _handle_dialog_which_one(request)
            else:
                # User doesn't want more info
                message = strings.INTENT_GENERAL_OK
                return ResponseBuilder.create_response(request, message=message)
        else:
            # Send user full article in a card
            return _handle_dialog_send_article(request)


def _handle_dialog_read_titles(request):
    """ Create a response with titles of articles about given company.
    :type request AlexaRequest"""
    ticker = request.get_slot_value('stockTicker')
    headings = FeedReader(ticker).get_articles_titles(limit=news_count)
    message = _build_read_titles_msg(headings, ticker)

    return ResponseBuilder \
        .create_response(request, message=message, is_ssml=True) \
        .with_dialog_confirm_intent()


def _build_read_titles_msg(headings, ticker):
    """Build SSML response text for read titles."""
    company = Ticker2Name.ticker_to_name(ticker)

    msg_body = ""
    ssml_strong_break = "<break time='700ms'/>"
    for heading in headings:
        msg_body += ssml_strong_break + heading + "."

    msg_intro = strings.INTENT_NEWS_ABOUT_COMPANY_INTRO.format(company)
    msg_end = ssml_strong_break + strings.INTENT_NEWS_ABOUT_COMPANY_ASK_MORE_INFO
    message = "<speak>" + msg_intro + msg_body + msg_end + "</speak>"
    return message


def _handle_dialog_which_one(request):
    """Create a response asking which article user wants to know about to get articleNo."""
    message = strings.INTENT_NEWS_ABOUT_COMPANY_ASK_ARTICLE_NO
    return ResponseBuilder.create_response(request, message=message) \
        .with_dialog_elicit_slot()


def _handle_dialog_send_article(request):
    """Create a response with card containing requested article."""
    reprompt = strings.INTENT_GENERAL_REPROMPT

    ticker = request.get_slot_value('stockTicker')
    company = Ticker2Name.ticker_to_name(ticker)
    article_no = int(request.get_slot_value('articleNo')) - 1
    # last news
    if article_no == -1:
        article_no = news_count - 1

    article_body = FeedReader(ticker).get_article_body(article_no)
    if article_body is None:
        # Article not found
        message = strings.INTENT_NEWS_ABOUT_COMPANY_FAIL_ARTICLE_NOT_FOUND
        return ResponseBuilder.create_response(request, message=message) \
            .with_reprompt(reprompt)

    # Build response
    message = strings.INTENT_NEWS_ABOUT_COMPANY_ARTICLE_SENT
    card_title = strings.INTENT_NEWS_ABOUT_COMPANY_ARTICLE_CARD_TITLE \
        .format(company)
    card_content = strings.INTENT_NEWS_ABOUT_COMPANY_ARTICLE_CARD_CONTENT \
        .format(article_body)
    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt) \
        .with_card(card_title, content=card_content)
