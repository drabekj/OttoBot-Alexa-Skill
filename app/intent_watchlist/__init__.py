from app import ResponseBuilder
from app.models import Stock, Watchlist
from app.utils.MyError import EntryExistsError
from app.utils.alexa.request import AlexaRequest
from app.utils.authentication import authenticated
from static import strings


# ReportStockWatchlistIntent
@authenticated
def handle_report_stock_watchlist(request):
    """:type request AlexaRequest"""
    user_id = request.get_user_id()

    # Query DB for watchlist data
    ticker_list = Watchlist.get_users_tickers(user_id)
    stocks = _get_stocks(ticker_list)
    """:type stocks list[Watchlist]"""

    # Prepare response
    if not stocks:
        message = strings.INTENT_WATCHLIST_EMPTY_MSG
    else:
        message = _build_report_msg(stocks)

    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)


def _build_report_msg(stocks):
    message = strings.INTENT_WATCHLIST_REPORT_MSG_INTRO
    for stock in stocks:
        message += strings.INTENT_WATCHLIST_REPORT_MSG_BODY \
            .format(stock.Ticker, stock.Close)

    return message


def _get_stocks(ticker_list):
    stocks = []
    for ticker in ticker_list:
        stocks.append(Stock.get_last(ticker))

    return stocks


# AddStockToWatchlistIntent
@authenticated
def handle_add_to_watchlist(request):
    """:type request AlexaRequest"""
    user_id = request.get_user_id()

    # Parse stock ticker (either slot or sessionAttribute)
    ticker = request.get_slot_value('stockTicker')
    if ticker is None:
        ticker = request.session.get('stockTicker', None)

    if ticker is None:
        message = strings.INTENT_ADDED_TO_WATCHLIST_FAIL.format(ticker)
        return ResponseBuilder.create_response(request, message=message) \
            .with_reprompt(strings.INTENT_GENERAL_REPROMPT)

    # Prepare response
    message = strings.INTENT_ADDED_TO_WATCHLIST.format(ticker)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    # add ticker to watchlist
    try:
        Watchlist(ticker, user_id).save()
    except EntryExistsError as e:
        message = strings.INTENT_ADDED_TO_WATCHLIST_EXISTS.format(ticker)

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)
