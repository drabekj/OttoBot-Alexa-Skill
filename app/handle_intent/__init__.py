from alexaresponse import ResponseBuilder


def handle_intent(request):
    message = """Intent will be implemented shortly, be patient"""
    reprompt_message = "What can I do for you?"

    return ResponseBuilder.create_response(message) \
        .with_reprompt(message=reprompt_message)
