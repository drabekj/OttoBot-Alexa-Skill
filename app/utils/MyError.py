class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class EntryExistsError(Error):
    """Exception raised when entry already exists and duplicates are not allowed.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class UnknownRequestError(Error):
    """Exception raised when unknown request is received.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class UnknownIntentError(Error):
    """Exception raised when unknown intent is received.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class UnknownStockError(Error):
    """Exception raised when unknown intent is received.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, ticker="", message=""):
        self.ticker = ticker
        self.message = message
