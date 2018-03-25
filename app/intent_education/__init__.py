import static.strings as strings
import static.strings_edu as strings_edu
from app import ResponseBuilder, AlexaRequest


def handle_education(request):
    """:type request AlexaRequest"""
    term = request.get_slot_value('term')

    message = {
        'Market Capitalization': strings_edu.TERM_MARKET_CAP,
        'Price Earnings Ratio': strings_edu.TERM_PE_RATIO,
        'Equity': strings_edu.TERM_EQUITY,
    }.get(term, strings.INTENT_EDU_IN_CONSTRUCTION.format(term))
    reprompt_message = strings.REQUEST_LAUNCH_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(message=reprompt_message)
