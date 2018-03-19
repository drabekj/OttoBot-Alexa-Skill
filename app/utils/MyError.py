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
