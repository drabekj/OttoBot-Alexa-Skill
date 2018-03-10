from alexaresponse import ResponseBuilder, AlexaRequest
from static import strings


def handle_get_stock_price_intent(request):
    """ :type request AlexaRequest"""
    message = strings.INTENT_STOCK_PRICE_MSG
    reprompt_message = strings.INTENT_STOCK_PRICE_REPROMPT

    ticker = request.get_slot_value(slot_name="stockTicker")
    close = 333.33

    return ResponseBuilder.create_response(message.format(ticker, close))\
        .with_reprompt(reprompt_message)
