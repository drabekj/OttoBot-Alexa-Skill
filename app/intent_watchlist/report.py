# ReportStockWatchlistIntent
from flask_sqlalchemy import BaseQuery

from app import ResponseBuilder, logger
from app.models import Watchlist, Stock
from app.utils import Ticker2Name
from app.utils.MyError import UnknownStockError
from app.utils.authentication import authenticated
from static import strings


@authenticated
def handle_report_stock_watchlist(request):
    """:type request AlexaRequest"""
    user_id = request.get_user_id()

    # Query DB for watchlist data
    ticker_list = Watchlist.get_users_tickers(user_id)
    changes = _get_stocks_24h_change(ticker_list)
    """:type stocks list[Watchlist]"""

    # Prepare response
    if not changes:
        message = strings.INTENT_WATCHLIST_EMPTY_MSG
    else:
        message = _build_report_msg(ticker_list, changes)

    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)


def _build_report_msg(ticker_list, changes):
    message = strings.INTENT_WATCHLIST_REPORT_MSG_INTRO
    for index, ticker in enumerate(ticker_list):
        try:
            if changes[index] < 0:
                movement = "down"
            else:
                movement = "up"

            company_name = Ticker2Name.ticker_to_name(ticker)
            message += strings.INTENT_WATCHLIST_REPORT_MSG_BODY \
                .format(company_name, movement, abs(changes[index]))
        except AttributeError:
            raise UnknownStockError()

    return message


def _get_stocks(ticker_list):
    stocks = []
    for ticker in ticker_list:
        data = Stock.get_last(ticker)
        if data is None:
            logger.error(
                f"Watchlist contains unknown stock ticker: " + str(ticker))
            raise UnknownStockError(ticker)
        stocks.append(data)

    return stocks


def _get_stocks_24h_change(ticker_list):
    """ :return: List of % 24h changes for stocks in ticker_list. """
    changes = []
    for ticker in ticker_list:
        last_2_stock_entries = Stock.get_nth_latest(ticker, n=2)
        """ :type Stock[] last_2_stock_entries """
        price_change = _compute_percent_change(last_2_stock_entries[0].close,
                                               last_2_stock_entries[1].close)

        if price_change is None:
            logger.error(
                f"Watchlist contains unknown stock ticker: " + str(ticker))
            raise UnknownStockError(ticker)
        changes.append(price_change)

    return changes


def _compute_percent_change(start_val, end_val):
    return 100 - 100 / start_val * end_val
