from alexaresponse import ResponseBuilder, AlexaRequest
from app.models import Stock
from static import strings


def handle_report_stock_watchlist(request):
    """ :type request AlexaRequest"""
    user_id = request.user_id()

    # Query DB for watchlist data

    message = strings.INTENT_WATCHLIST_REPORT_MSG
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(message)\
        .with_reprompt(reprompt_message)
