import unittest
from textnode import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_basic(self):
        t = "This is text with [](www.noAltText.com) blah blah [NoLink]() and []() what about [] or () a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        print(extract_markdown_links(t))

if __name__ == "__main__":
    unittest.main()