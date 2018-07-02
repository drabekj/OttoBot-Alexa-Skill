from app import ResponseBuilder
from app.utils.Sentiment import Analyst
from static import strings


def handle_recommendation(request):
    """
        Generate response to intent type RecommendationIntent with the analytics recommendation for a particular stock.
        :type request AlexaRequest
        :return: JSON response including a recommendation what the analytics think about that stock
    """
    ticker = request.get_slot_value(slot_name="stockTicker").upper()
    recommendation = Analyst(ticker).recommendation()

    message = "Analysts recommendation factor is {0}".format(recommendation)
    response = ResponseBuilder.create_response(request, message=message)

    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return response.with_reprompt(reprompt_message)
