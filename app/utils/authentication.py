from app import handle_error_states
from app.models import User
from app.utils import FacebookApi
from app.utils.alexa.request import AlexaRequest


def authenticated(func):
    """
    Check if user is authenticated (has accessToken).
    If accessToken is not present build response handle_not_authenticated,
    If user not yet in DB save it to the user table.

    """

    def check_access_token(alexafied_request):
        """ :type alexafied_request AlexaRequest"""
        try:
            access_token = alexafied_request.access_token()
        except KeyError as e:
            print("User is probably not authenticated. error: " + str(e) + "missing")
            return handle_error_states \
                .handle_not_authenticated(alexafied_request)

        _remember_user_id(alexafied_request, access_token)
        return func(alexafied_request)

    return check_access_token


def _remember_user_id(alexafied_request, access_token):
    """ :type alexafied_request AlexaRequest"""
    # get user id and name from Facebook
    user = FacebookApi.get_me(access_token)

    # save user to DB if not already there
    User(user['id'], user['name']).save()

    # set session variables
    alexafied_request.set_user(user)

    return alexafied_request
