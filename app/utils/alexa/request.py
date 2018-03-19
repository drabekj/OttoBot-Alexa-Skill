from flask import request


# Decorator
def alexa_request(func):
    """
    Convert the incoming request into Request type.
    """

    def alexafy_request():
        req_obj = AlexaRequest(request.data)
        return func(req_obj)

    return alexafy_request


class AlexaRequest(object):
    """
    Simple wrapper around the JSON request
    received by the module
    """

    def __init__(self, request_dict, metadata=None):
        self.request = request_dict
        self.metadata = metadata or {}
        self.session = self.request.get('session', {}).get('attributes', {})
        if self.intent_name():
            self.slots = self.get_slot_map()

    def request_type(self):
        return self.request["request"]["type"]

    def intent_name(self):
        if "request" not in self.request or \
                "intent" not in self.request["request"]:
            return None
        return self.request["request"]["intent"]["name"]

    def is_intent(self):
        if self.intent_name() is None:
            return False
        return True

    def user_id(self):
        return self.request["session"]["user"]["userId"]

    def access_token(self):
        return self.request['session']['user']['accessToken']

    def session_id(self):
        return self.request["session"]["sessionId"]

    def get_slot_value(self, slot_name):
        try:
            return self.request["request"]["intent"]["slots"][slot_name][
                "value"]
        except:
            """Value not found"""
            return None

    def get_slot_names(self):
        try:
            return self.request['request']['intent']['slots'].keys()
        except:
            return []

    def get_slot_map(self):
        return {slot_name: self.get_slot_value(slot_name)
                for slot_name in self.get_slot_names()}
