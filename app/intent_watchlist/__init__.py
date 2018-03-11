from alexaresponse import ResponseBuilder, AlexaRequest
from app.models import Stock, Watchlist
from static import strings


def handle_report_stock_watchlist(request):
    """:type request AlexaRequest"""
    user_id = request.user_id()

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

    return ResponseBuilder.create_response(message) \
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
