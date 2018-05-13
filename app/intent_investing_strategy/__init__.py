import random

from app import ResponseBuilder
from static import strings, strings_edu


def handle_investing_strategy(request):
    """
    Generate response to intent type InvestingStrategyIntent with explanation of a random investing strategy.
    :type request AlexaRequest
    :return: JSON response including investing strategy name and explanation
    """
    strategies = strings_edu.STRATEGIES['data']
    pick = random.randint(0, len(strategies) - 1)

    strategy_name = strategies[pick]['name']
    strategy_content = strategies[pick]['content']

    message = strings.INTENT_INVEST_STRAT_MSG.format(strategy_name, strategy_content)
    reprompt_message = strings.INTENT_GENERAL_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(reprompt_message)
