from sqlalchemy.util import NoneType

from app import ResponseBuilder, logger
from app.models import Stock
from static import strings


def handle_market_cap(request):
    """
    Generate response to intent type MarketCapIntent with the current market cap of the ticker.
    :type request AlexaRequest
    :return: JSON response including market cap of the ticker
    """
    ticker = request.get_slot_value(slot_name="stockTicker").upper()

    # Query DB for stock data
    company_stats = Stock.get_stats(ticker)
    market_cap = company_stats.get('marketcap', None)
    company_name = company_stats.get('companyName', ticker)

    if type(market_cap) is NoneType:
        logger.error(f"There was an error getting market capitalization for {company_name}")
        message = strings.INTENT_MARKET_CAP_MSG_FAIL.format(ticker)
        response = ResponseBuilder.create_response(request, message=message)
    else:
        message = strings.INTENT_MARKET_CAP_MSG.format(company_name, market_cap)
        response = ResponseBuilder.create_response(request, message=message) \
            .set_session('stockTicker', ticker)

    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return response.with_reprompt(reprompt_message)
