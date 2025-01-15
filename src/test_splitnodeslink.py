import unittest
from textnode import TextNode, TextType, split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_basic(self):
        print("============= Doing basic tests on split_nodes_image(test) ===========================")
        nl = [
            TextNode(
                "This is text with [](www.noAltText.com) blah blah [NoLink]() and []() what about [] or () a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL
            )
        ]

        print(split_nodes_link(nl))
    
if __name__ == "__main__":
    unittest.main()

