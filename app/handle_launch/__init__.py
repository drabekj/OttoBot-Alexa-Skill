import static.strings as strings
from app import ResponseBuilder


def handle_launch(request):
    """
    Generate response for a launch request like 'Open OttoBot'.
    :param request: incoming parsed Alexa request
    :return: Generated JSON welcome response answer
    """
    message = strings.REQUEST_LAUNCH_MSG
    reprompt_message = strings.REQUEST_LAUNCH_REPROMPT

    return ResponseBuilder.create_response(request, message=message) \
        .with_reprompt(message=reprompt_message)
