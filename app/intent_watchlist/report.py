# ReportStockWatchlistIntent
from flask_sqlalchemy import BaseQuery

from app import ResponseBuilder, logger
from app.models import Watchlist, Stock
from app.utils.MyError import UnknownStockError
from app.utils.authentication import authenticated
from static import strings


@authenticated
def handle_report_stock_watchlist(request):
    """:type request AlexaRequest"""
    user_id = request.get_user_id()

    # Query DB for watchlist data
    ticker_list = Watchlist.get_users_tickers(user_id)
    stocks = _get_stocks_24h_change(ticker_list)
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
        try:
            message += strings.INTENT_WATCHLIST_REPORT_MSG_BODY \
                .format(stock.Ticker, stock.Close)
        except AttributeError:
            raise UnknownStockError()

    return message


def _get_stocks(ticker_list):
    stocks = []
    for ticker in ticker_list:
        data = Stock.get_last(ticker)
        if data is None:
            logger.error(f"Watchlist contains unknown stock ticker: " + str(ticker))
            raise UnknownStockError(ticker)
        stocks.append(data)

    return stocks


def _get_stocks_24h_change(ticker_list):
    stocks = []
    for ticker in ticker_list:
        last_2_stock_entries = Stock.get_last_n(ticker, n=2)
        """  :type last_2_stock_entries BaseQuery """
        count = last_2_stock_entries.count()
        all = last_2_stock_entries.all()
        first = last_2_stock_entries.first()
        """ :type Stock[] last_2_stock_entries """
        price_change = last_2_stock_entries[0].Close - last_2_stock_entries[1].Close

        if price_change is None:
            logger.error(f"Watchlist contains unknown stock ticker: " + str(ticker))
            raise UnknownStockError(ticker)
        stocks.append(price_change)

    return stocks