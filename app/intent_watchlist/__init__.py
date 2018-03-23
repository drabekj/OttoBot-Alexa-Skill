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
        logger.exception("No valid ticker provided")
        message = strings.INTENT_ADDED_TO_WATCHLIST_FAIL
        return ResponseBuilder.create_response(request, message=message) \
            .with_reprompt(strings.INTENT_GENERAL_REPROMPT)

    # Ask user to confirm ticker add
    message = strings.INTENT_ADD_TO_WATCHLIST_ASK_CONFIRMATION.format(ticker)
    return ResponseBuilder.create_response(request, message) \
        .with_dialog_confirm_intent()


def _handle_dialog_add_in_progress(request):
    """:type request AlexaRequest"""
    logger.debug("dialogState IN_PROGRESS")

    if request.get_intent_confirmation_status() == "CONFIRMED":
        return _add_ticker_to_watchlist(request)
    else:
        message = strings.INTENT_ADD_TO_WATCHLIST_DENIED
        return ResponseBuilder.create_response(request, message=message)


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

# RemoveStockFromWatchlistIntent
@authenticated
def handle_remove_from_watchlist(request):
    """:type request AlexaRequest"""

    if request.dialog_state() == "STARTED":
        return _handle_dialog_remove_started(request)
    elif request.dialog_state() == "IN_PROGRESS":
        return _handle_dialog_remove_in_progress(request)
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


def _handle_dialog_remove_started(request):
    """:type request AlexaRequest"""
    logger.debug("dialogState STARTED")
    user_id = request.user_id()

    # Check if ticker is provided
    try:
        ticker = _check_valid_ticker_provided(request)
    except AttributeError as e:
        logger.exception("No valid ticker provided")
        message = strings.INTENT_REMOVE_FROM_WATCHLIST_FAIL
        return ResponseBuilder.create_response(request, message=message) \
            .with_reprompt(strings.INTENT_GENERAL_REPROMPT)

    # Check if stock is in users Watchlist
    is_in_watchlist = Watchlist.ticker_in_watchlist_exists(user_id, ticker)

    # Inform that stock not in watchlist, or ask user to confirm ticker remove
    if is_in_watchlist:
        logger.debug(f"Ask confirmation: remove stock {ticker} from user:{user_id} watchlist")
        message = strings.INTENT_REMOVE_FROM_WATCHLIST_ASK_CONFIRMATION \
            .format(ticker)
        return ResponseBuilder.create_response(request, message) \
            .with_dialog_confirm_intent()
    else:
        logger.debug(f"Trying to remove stock {ticker}, which is not in wathclist")
        message = strings.INTENT_REMOVE_FROM_WATCHLIST_NOT_THERE.format(ticker)
        return ResponseBuilder.create_response(request, message)


def _handle_dialog_remove_in_progress(request):
    """:type request AlexaRequest"""
    logger.debug("dialogState IN_PROGRESS")

    if request.get_intent_confirmation_status() == "CONFIRMED":
        return _remove_ticker_from_watchlist(request)
    else:
        logger.debug(f"Deny deleting of stock from watchlist")
        message = strings.INTENT_REMOVE_FROM_WATCHLIST_DENIED
        return ResponseBuilder.create_response(request, message=message)


def _remove_ticker_from_watchlist(request):
    """Remove ticker from users Watchlist if there and build response.
        :type request AlexaRequest
    """
    user_id = request.get_user_id()
    ticker = request.get_slot_value('stockTicker')
    if ticker == "NONE":
        ticker = request.get_session_attribute('stockTicker')

    message = strings.INTENT_REMOVE_FROM_WATCHLIST_CONFIRMED.format(ticker)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    # Delete stock from watchlist
    try:
        Watchlist(ticker, user_id).delete()
    except EntryExistsError as e:
        logger.exception(f"Error while deleting ticker {ticker} from Watchlist")

    logger.debug(f"Deleted stock {ticker} from user:{user_id} watchlist")
    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)


# Helper
def _check_valid_ticker_provided(request):
    ticker = request.get_slot_value('stockTicker')

    if ticker is None:
        ticker = request.session.get('stockTicker', None)
    if ticker is None:
        raise AttributeError("No valid ticker provided")

    return ticker