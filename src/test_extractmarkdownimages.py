import unittest
from textnode import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_basic(self):
        t = "This ![FAKE] is yada [text] with ![]() a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg).  Blah blah ![](www.link.com)"
        print(extract_markdown_images(t))


if __name__ == "__main__":
    unittest.main()