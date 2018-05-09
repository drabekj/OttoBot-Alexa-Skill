import static.strings as strings
import static.strings_edu as strings_edu
from app import ResponseBuilder, AlexaRequest


def handle_education(request):
    """:type request AlexaRequest"""
    term = request.get_slot_value('term')

    message = {
        'Liquid market': strings_edu.TERM_LIQUIDITY,
        'Yield': strings_edu.TERM_YIELD,
        'Spread': strings_edu.TERM_SPREAD,
        'Dividend': strings_edu.TERM_DIVIDEND,
        'Broker': strings_edu.TERM_BROKER,
        'Bear Market': strings_edu.TERM_BEAR_MARKET,
        'Bull Market': strings_edu.TERM_BULL_MARKET,
        'BID': strings_edu.TERM_BID,
        'ASK': strings_edu.TERM_ASK,
        'Price Earnings Ratio': strings_edu.TERM_PE_RATIO,
        'Market Capitalization': strings_edu.TERM_MARKET_CAP,
        'Equity': strings_edu.TERM_EQUITY,
        'IPO': strings_edu.TERM_IPO,
    }.get(term, strings.INTENT_EDU_IN_CONSTRUCTION.format(term))
    reprompt_message = strings.REQUEST_LAUNCH_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(message=reprompt_message)
