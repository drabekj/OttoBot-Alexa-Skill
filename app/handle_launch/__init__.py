from alexaresponse import ResponseBuilder
import static.strings as strings


def handle_launch(request):
    message = strings.INTENT_LAUNCH_MSG
    reprompt_message = strings.INTENT_LAUNCH_REPROMPT

    return ResponseBuilder.create_response(message) \
        .with_reprompt(message=reprompt_message)
