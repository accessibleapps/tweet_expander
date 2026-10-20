"""Exercise the real URL dispatcher without contacting provider services."""

import importlib
import sys
import unittest
from unittest.mock import Mock, patch


class TweetExpanderTests(unittest.TestCase):
    def setUp(self):
        twitlonger = Mock()
        twishort = Mock()
        with patch.dict(sys.modules, {"twitlonger": twitlonger, "twishort": twishort}):
            sys.modules.pop("tweet_expander", None)
            module = importlib.import_module("tweet_expander")
        self.expander = module.TweetExpander()

    def test_supported_urls_return_provider_text(self):
        cases = (
            ("https://twishort.com/abc123", self.expander.twishort_API),
            ("http://www.twishort.com/abc123", self.expander.twishort_API),
            ("https://tl.gd/abc123", self.expander.twitlonger_API),
            ("https://twitlonger.com/show/abc123", self.expander.twitlonger_API),
        )
        for url, provider in cases:
            with self.subTest(url=url):
                provider.reset_mock()
                provider.get_text.return_value = "expanded text"

                self.assertEqual(self.expander.retrieve_text(url), "expanded text")

                provider.get_text.assert_called_once_with(url)

    def test_unsupported_url_does_not_contact_a_provider(self):
        self.assertIsNone(self.expander.retrieve_text("https://example.test/post"))

        self.expander.twishort_API.get_text.assert_not_called()
        self.expander.twitlonger_API.get_text.assert_not_called()


if __name__ == "__main__":
    unittest.main()
