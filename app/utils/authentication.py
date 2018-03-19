from app import handle_error_states
from app.models import User
from app.utils import FacebookApi


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
            print("User is probably not authenticated. error: " + str(e))
            return handle_error_states \
                .handle_not_authenticated(alexafied_request)

        # add it to the Users table if not already there
        user = FacebookApi.get_me(access_token)
        User(user['id'], user['name']).save()
        return func(alexafied_request)

    return check_access_token
