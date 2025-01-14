import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_propsToHtml(self):
        node1 = HTMLNode("<a>", "This is some text", None, {"href": "https://www.google.com", "src": "SomethingBlahBlah"})
        node2 = HTMLNode("<a>", "This is some text")
        print(node1)
        print(node1.props_to_html())
        print(node2.props_to_html())
        print("--")
        #node1.to_html()
    
if __name__ == "__main__":
    unittest.main()