import unittest
from textnode import TextNode, TextType, split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_basic(self):
        print("============= Doing basic tests on split_nodes_image(test) ===========================")
        nl = [
            TextNode(
                "This ![FAKE] is yada [text] with ![]() a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg).  Blah blah ![](www.link.com)",
                TextType.NORMAL
            ),
            TextNode(
                "![A img](www.paganunk.com) was once a thing.  Oh the humanity.",
                TextType.NORMAL
            )
        ]

        print(split_nodes_image(nl))

if __name__ == "__main__":
    unittest.main()