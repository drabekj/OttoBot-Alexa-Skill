import static.strings as strings
from app import ResponseBuilder


def handle_launch(request):
    message = strings.REQUEST_LAUNCH_MSG
    reprompt_message = strings.REQUEST_LAUNCH_REPROMPT

    return ResponseBuilder.create_response(message) \
        .with_reprompt(message=reprompt_message)
