import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic(self):
        node1 = LeafNode("p", "This is a paragraph of text")
        print(node1)
        print(node1.to_html())
    def test_noTag(self):
        node1 = LeafNode(None, "This is some text without a tag")
        print(node1)
        print(node1.to_html())
    def test_with_props(self):
        node1 = LeafNode("a", "This is link text", {"href": "https://linky.com"})
        print(node1)
        print(node1.to_html())

if __name__ == "__main__":
    unittest.main()