from app import ResponseBuilder, logger
from app.models import Stock, Watchlist
from app.utils import MyError
from app.utils.MyError import EntryExistsError, UnknownStockError
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


# AddStockToWatchlistIntent
@authenticated
def handle_add_to_watchlist(request):
    """:type request AlexaRequest"""

    if request.dialog_state() == "STARTED":
        return _handle_dialog_add_started(request)
    elif request.dialog_state() == "IN_PROGRESS":
        return _handle_dialog_add_in_progress(request)
    elif request.dialog_state() == "COMPLETED":
        # TODO
        return ResponseBuilder.create_response(request, "Add to watchlist dialog completed! ")
    elif request.dialog_state() == "":
        # TODO
        print("LOG-d: dialogState not included")
        return ResponseBuilder.create_response(request, "Add to watchlist dialog state empty! ")
    else:
        print("LOG-d: dialogState else")
        # TODO
        print("LOG-d: dialogState not included")
        return ResponseBuilder.create_response(request, "Add to watchlist dialog state ELSE! ")


def _handle_dialog_add_started(request):
    """:type request AlexaRequest"""
    print("LOG-d: dialogState STARTED")

    # Check if ticker is provided
    try:
        ticker = _check_valid_ticker_provided(request)
    except AttributeError as e:
        print("LOG-e: no valid ticker provided")
        message = strings.INTENT_ADDED_TO_WATCHLIST_FAIL
        return ResponseBuilder.create_response(request, message=message) \
            .with_reprompt(strings.INTENT_GENERAL_REPROMPT)

    # Ask user to confirm ticker add
    message = strings.INTENT_ADD_TO_WATCHLIST_ASK_CONFIRMATION.format(ticker)
    return ResponseBuilder.create_response(request, message) \
        .with_dialog_confirm_intent()


def _handle_dialog_add_in_progress(request):
    """:type request AlexaRequest"""
    print("LOG-d: dialogState IN_PROGRESS")

    if request.get_intent_confirmation_status() == "CONFIRMED":
        return _add_ticker_to_watchlist(request)
    else:
        message = strings.INTENT_ADD_TO_WATCHLIST_DENIED
        return ResponseBuilder.create_response(request, message=message)


def _check_valid_ticker_provided(request):
    ticker = request.get_slot_value('stockTicker')

    if ticker is None:
        ticker = request.session.get('stockTicker', None)
    if ticker is None:
        raise AttributeError("no valid ticker provided")

    return ticker


def _add_ticker_to_watchlist(request):
    """Add ticker to users Watchlist if not already there and build response.
        :type request AlexaRequest
    """
    user_id = request.get_user_id()
    ticker = request.get_slot_value('stockTicker')
    if ticker == "NONE":
        ticker = request.get_session_attribute('stockTicker')

    message = strings.INTENT_ADD_TO_WATCHLIST_CONFIRMED.format(ticker)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    # Check if ticker not already in Watchlist
    try:
        Watchlist(ticker, user_id).save()
    except EntryExistsError as e:
        message = strings.INTENT_ADDED_TO_WATCHLIST_EXISTS.format(ticker)

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)
