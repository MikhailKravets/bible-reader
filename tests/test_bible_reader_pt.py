import pytest

from requests.exceptions import Timeout

from reader.bibles.bible import BibleReader
from reader.errors import APIError
from reader.models import Bible
from tests.testdata.bible import SUCCESS_RESPONSE


def test_instance_creation():
    url = "http://test.url"
    reader = BibleReader(url=url)

    assert reader.url == url


def test_get(bible_reader, get_params, mock_request):
    book, chapter, verse = get_params
    resp = bible_reader.get(book, chapter, verse)

    assert isinstance(resp, Bible)

    assert resp.reference == SUCCESS_RESPONSE['reference']
    assert resp.translation_note == SUCCESS_RESPONSE['translation_note']
    assert len(resp.verses) == 1

    mock_request.assert_called_once()


def test_get_api_error(bible_reader, get_params, mock_request_api_error):
    with pytest.raises(APIError):
        bible_reader.get(*get_params)


def test_get_timeout(bible_reader, get_params, mock_request_timeout_error):
    with pytest.raises(Timeout):
        bible_reader.get(*get_params)
