import facebook

from app import logger


def get_me(access_token):
    """ :return dict {id, name}"""
    graph = facebook.GraphAPI(access_token=access_token, version=2.7)

    try:
        user = graph.get_object("me")
    except facebook.GraphAPIError as e:
        logger.exception("Expired Facebook access token")
        raise e

    return user
