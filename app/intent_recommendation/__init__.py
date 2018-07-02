from app import ResponseBuilder
from app.utils.Sentiment import Analyst
from static import strings
from app import logger


def handle_recommendation(request):
    """
        Generate response to intent type RecommendationIntent with the analytics recommendation for a particular stock.
        :type request AlexaRequest
        :return: JSON response including a recommendation what the analytics think about that stock
    """
    ticker = request.get_slot_value(slot_name="stockTicker").upper()
    recommendation = Analyst(ticker).recommendation()

    logger.info(
        f"recommendationMean for {ticker} is {recommendation}")

    # pick right response based on recommendation mean rating
    if recommendation is None:
        message = strings.INTENT_RCMD_NO_RCMD
    elif _in_interval(recommendation, 1, 1.8):
        message = strings.INTENT_RCMD_STRONG_BUY
    elif _in_interval(recommendation, 1.8, 2.2):
        message = strings.INTENT_RCMD_BUY
    elif _in_interval(recommendation, 2.2, 2.8):
        message = strings.INTENT_RCMD_OPT_HOLD
    elif _in_interval(recommendation, 2.8, 3.2):
        message = strings.INTENT_RCMD_HOLD
    elif _in_interval(recommendation, 3.2, 3.8):
        message = strings.INTENT_RCMD_PES_HOLD
    elif _in_interval(recommendation, 3.8, 4.2):
        message = strings.INTENT_RCMD_SELL
    elif _in_interval(recommendation, 4.2, 5):
        message = strings.INTENT_RCMD_STRONG_SELL

    response = ResponseBuilder.create_response(request, message=message)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return response.with_reprompt(reprompt_message)


def _in_interval(value, low, up):
    """check if value is in an inclusive interval"""
    if low <= value <= up:
        return True
    else:
        return False
