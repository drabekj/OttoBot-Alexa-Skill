from sqlalchemy.util import NoneType

from alexaresponse import ResponseBuilder, AlexaRequest
from app.models import Stock
from static import strings


def handle_get_stock_price_intent(request):
    """ :type request AlexaRequest"""
    ticker = request.get_slot_value(slot_name="stockTicker")

    # Query DB for stock data
    stock = Stock.get_last(ticker)

    if type(stock) is NoneType:
        print("LOG-e: There was a error getting data for {}".format(ticker))
        message = strings.INTENT_STOCK_PRICE_MSG_FAIL.format(ticker)
    else:
        message = strings.INTENT_STOCK_PRICE_MSG.format(ticker, stock.Close)
    reprompt_message = strings.INTENT_STOCK_PRICE_REPROMPT

    return ResponseBuilder.create_response(message)\
        .with_reprompt(reprompt_message)