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

    def dialog_state(self):
        if self.is_intent():
            return self.request["request"].get('dialogState', {})

    def user_id(self):
        return self.session["userId"]

    def access_token(self):
        return self.request['session']['user']['accessToken']

    def session_id(self):
        return self.request["session"]["sessionId"]

    def get_session_attribute(self, attribut_key):
        return self.request["session"]["attributes"][attribut_key]

    def get_slot_value(self, slot_name):
        """
        Get the corrected slot value from resolutions, if no match found,
        fallback to raw slot value.
        """
        try:
            slot = self.request["request"]["intent"]["slots"][slot_name]
            resolutions = slot.get('resolutions', {}) \
                .get('resolutionsPerAuthority', {})

            if resolutions and resolutions[0]['status']['code'] == "ER_SUCCESS_MATCH":
                value = resolutions[0]['values'][0]['value']['name']
            else:
                value = self._get_slot_value_fallback(slot_name)

            return value
        except Exception as e:
            """Value not found"""
            raise e
            logger
            return None

    def _get_slot_value_fallback(self, slot_name):
        """
        Get raw slot value. You should use "get_slot_value instead."
        """
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

    def set_user(self, user):
        self.session['userId'] = user['id']
        self.session['userName'] = user['name']

    def get_user_id(self):
        return self.session['userId']

    def get_user_name(self):
        return self.session['userName']

    def get_intent_confirmation_status(self):
        return self.request['request'].get('intent', {}).get('confirmationStatus', None)
