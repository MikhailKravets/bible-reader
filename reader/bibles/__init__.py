import typing
from abc import ABC, abstractmethod

import requests

from reader.constants import REQUEST_TIMEOUT
from reader.errors import APIError
from reader.models import Bible


class AbstractReader(ABC):
    """Abstract interface for all possible readers"""

    @abstractmethod
    def get(self, *args, **kwargs) -> Bible:
        """Get the data from the API for the given arguments

        Returns:
            Bible object with the verses
        """

    @abstractmethod
    def prepare_url(self, *args, **kwargs) -> str:
        """Prepare url for the given arguments

        Returns:
            Built URL to the API endpoint
        """

    @abstractmethod
    def prepare_response(self, data: typing.Dict[str, typing.Any]) -> Bible:
        """Prepare Bible object from the given data

        Returns:
            Bible object with the verses
        """


class BaseReader(AbstractReader):
    """Base reader class to implement
    base reading functionality

    Args:
        url: url to the API endpoint
    """

    def __init__(self, url: str):
        self.url = url

    def request(self, url: str):
        """Request the remote API and prepare the response

        Args:
            url: url to request

        Returns:
            Bible object with the verses
        """
        resp = requests.get(url, headers={'Content-Type': 'application/json'}, timeout=REQUEST_TIMEOUT)

        if not resp.ok:
            raise APIError(f"API error [{resp.status_code}]: {resp.json()}")

        data = resp.json()

        return self.prepare_response(data)
