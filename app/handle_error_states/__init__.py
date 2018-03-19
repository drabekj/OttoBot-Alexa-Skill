from app.utils import alexaresponse as alexa
from static import strings


def handle_not_authenticated(request):
    """ Build a response for case where user has not
    linked the account in Alexa App.
    """
    message = strings.ERROR_NOT_AUTHENTICATED
    reprompt_message = strings.ERROR_NOT_AUTHENTICATED_REPROMPT

    return alexa.ResponseBuilder.create_response(message) \
        .with_reprompt(message=reprompt_message) \
        .with_card("", card_type="LinkAccount")
