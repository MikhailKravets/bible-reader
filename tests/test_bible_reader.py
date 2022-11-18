# import unittest
# from unittest.mock import patch, MagicMock
#
# from requests.exceptions import Timeout
#
# from reader.bibles.bible import BibleReader
# from reader.errors import APIError
# from reader.models import Bible
# from tests.testdata.bible import SUCCESS_RESPONSE
#
#
# class TestBibleReader(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.book = "john"
#         self.chapter = 3
#         self.verse = 16
#
#         self.reader = BibleReader()
#
#     def test_instance_creation(self):
#         url = "http://test.url"
#         reader = BibleReader(url=url)
#         self.assertEqual(reader.url, url)
#
#     @patch("reader.bibles.requests.get")
#     def test_get(self, get):
#         mock = MagicMock()
#         get.return_value = mock
#         mock.ok = True
#         mock.json.return_value = SUCCESS_RESPONSE
#
#         response = self.reader.get(self.book, self.chapter, self.verse)
#
#         self.assertIsInstance(response, Bible)
#         self.assertEqual(response.reference, 'John 3:16')
#         self.assertEqual(response.translation_name, 'World English Bible')
#         self.assertEqual(response.translation_note, 'Public Domain')
#
#         self.assertEqual(len(response.verses), 1)
#         get.assert_called_once()
#
#     @patch("reader.bibles.requests.get")
#     def test_get_api_error(self, get):
#         mock = MagicMock()
#         get.return_value = mock
#         mock.ok = False
#         mock.json.return_value = {"status": "error"}
#
#         with self.assertRaises(APIError):
#             self.reader.get(self.book, self.chapter, self.verse)
#
#     @patch("reader.bibles.requests.get")
#     def test_get_timeout(self, get):
#         get.side_effect = Timeout
#
#         with self.assertRaises(Timeout):
#             self.reader.get(self.book, self.chapter, self.verse)
