from unittest.mock import Mock

import pytest
import requests

from requests.exceptions import Timeout

from reader.bibles.bible import BibleReader
from tests.testdata.bible import SUCCESS_RESPONSE


@pytest.fixture(scope="package")
def bible_reader():
    return BibleReader()


@pytest.fixture(scope="package")
def get_params():
    book = "john"
    chapter = 2
    verse = 16
    return book, chapter, verse


@pytest.fixture(scope="function")
def mock_request(monkeypatch):
    p = Mock()
    p.return_value.ok = True
    p.return_value.json.return_value = SUCCESS_RESPONSE
    monkeypatch.setattr(requests, "get", p)

    yield p


@pytest.fixture(scope="function")
def mock_request_api_error(monkeypatch):
    p = Mock()
    p.return_value.ok = False
    p.return_value.json.return_value = {"success": "error"}
    monkeypatch.setattr(requests, "get", p)

    yield p


@pytest.fixture(scope="function")
def mock_request_timeout_error(monkeypatch):
    p = Mock()
    p.side_effect = Timeout("test timeout")
    monkeypatch.setattr(requests, "get", p)

    yield p
