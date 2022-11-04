
class BibleError(Exception):
    """Base Bible Error"""


class APIError(BibleError):
    """Raise when API response is not successful"""
