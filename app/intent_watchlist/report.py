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
    """
    Generate response to intent type ReportStockWatchlistIntent reporting the current portfolio performance.
    :type request AlexaRequest
    :return: JSON response including the performance report.
    """
    user_id = request.get_user_id()

    # Query DB for watchlist data
    ticker_list = Watchlist.get_users_tickers(user_id)
    changes = _get_stocks_24h_change(ticker_list)

    if len(ticker_list) > 2:
        max_idx = _find_biggest_value(changes)
        gainer_ticker = ticker_list.pop(max_idx)
        gainer_value = changes.pop(max_idx)
        min_idx = _find_smallest_value(changes)
        loser_ticker = ticker_list.pop(min_idx)
        loser_value = changes.pop(min_idx)

        gainer_message = strings.INTENT_WATCHLIST_REPORT_TOP_STOCK.format(
            Ticker2Name.ticker_to_name(gainer_ticker),
            _get_movement_direction(gainer_value),
            abs(gainer_value))
        loser_message = strings.INTENT_WATCHLIST_REPORT_WORST_STOCK.format(
            Ticker2Name.ticker_to_name(loser_ticker),
            _get_movement_direction(loser_value),
            abs(loser_value))

        message = gainer_message + loser_message + _build_report_msg(ticker_list, changes)
    elif len(ticker_list) == 2 or len(ticker_list) == 1:
        message = _build_report_msg(ticker_list, changes)
    else:
        message = strings.INTENT_WATCHLIST_EMPTY_MSG

    reprompt_message = strings.INTENT_GENERAL_REPROMPT
    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)


def _build_report_msg(ticker_list, changes):
    message = strings.INTENT_WATCHLIST_REPORT_MSG_INTRO
    for index, ticker in enumerate(ticker_list):
        try:
            movement = _get_movement_direction(changes[index])

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
    changes = Stock.get_change_batch(ticker_list)
    return changes


def _compute_percent_change(start_val, end_val):
    return 100 - 100 / start_val * end_val


def _find_biggest_value(list):
    """
    Get the intex of the largest value in list of values
    :return: -1 if list empty, otherwise index of biggest value
    """
    if len(list) < 1:
        return -1

    max = 0
    for idx, val in enumerate(list):
        if val > list[max]:
            max = idx

    return max


def _find_smallest_value(list):
    """
    Get the intex of the smallest value in list of values
    :return: -1 if list empty, otherwise index of smallest value
    """
    if len(list) < 1:
        return -1

    min = 0
    for idx, val in enumerate(list):
        if val < list[min]:
            min= idx

    return min


def _get_movement_direction(value):
    if value < 0:
        movement = "down"
    else:
        movement = "up"

    return movement
