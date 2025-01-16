import unittest
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_basic(self):
        nodeList = [TextNode("Plain Text", TextType.NORMAL), TextNode("Bold Text", TextType.BOLD), TextNode("Italic Text", TextType.ITALIC), TextNode("Code Text", TextType.CODE),TextNode("Link Text", TextType.LINK, "https://www.google.com"), TextNode("Image Text", TextType.IMAGE, "https://www.linktoimage.com")]
        for n in nodeList:
            hn = n.to_html_node()
            print(hn.to_html())
    def test_exceptions(self):
        tn = TextNode("Invalid type", "RandomString")
        try:
            hn = tn.to_html_node()
            print(hn.to_html)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    unittest.main()