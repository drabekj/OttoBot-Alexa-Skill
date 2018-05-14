from app import ResponseBuilder, logger
from static import strings


def handle_help_intent(request):
    """
    Generate response to intent type HelpIntent which presents the available futures to the confused user.
    :type request AlexaRequest
    :return: JSON response including introduced capabilities of the skill
    """
    logger.info("Help requested by the user")

    message = strings.INTENT_HELP
    reprompt_message = strings.INTENT_GENERAL_REPROMPT
    return ResponseBuilder.create_response(request, message=message)\
        .with_reprompt(reprompt_message)
