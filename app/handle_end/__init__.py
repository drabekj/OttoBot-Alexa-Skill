import static.strings as strings
import app.utils.alexa.response as response


def handle_end(request):
    """
    Handle end session request like 'Alexa stop'.
    :param request: incoming parsed Alexa request
    :return: Generated JSON response goodbye answer
    """
    message = strings.REQUEST_END_MSG

    return response.ResponseBuilder.create_response(request, message=message,
                                               end_session=True)
