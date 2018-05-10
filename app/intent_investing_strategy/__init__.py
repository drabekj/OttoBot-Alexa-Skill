import random

from app import ResponseBuilder
from static import strings, strings_edu


def handle_investing_strategy(request):
    """ :type request AlexaRequest"""
    strategies = strings_edu.STRATEGIES['data']
    pick = random.randint(0, len(strategies) - 1)

    strategy_name = strategies[pick]['name']
    strategy_content = strategies[pick]['content']

    message = strings.INTENT_INVEST_STRAT_MSG.format(strategy_name, strategy_content)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)
