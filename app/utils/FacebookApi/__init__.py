import facebook


def get_me(access_token):
    """ :return dict {id, name}"""
    graph = facebook.GraphAPI(access_token=access_token, version=2.7)
    user = graph.get_object("me")
    return user
