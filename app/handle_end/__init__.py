import static.strings as strings
import app.utils.alexa.response as response


def handle_end(request):
    message = strings.REQUEST_END_MSG

    return response.ResponseBuilder.create_response(request, message=message,
                                               end_session=True)
