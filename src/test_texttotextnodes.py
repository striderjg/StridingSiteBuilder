import unittest
from textnode import TextNode, TextType, text_to_textnodes

class TestTextToTextnodes(unittest.TestCase):
    def test_basic(self):
        print("=============== Doing basic tests on text_to_Textnodes(text)")
        t = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        t2 = "![Start image](https://linktostartimage.com) is a line that **starts** with a image at [link to img](https://linktostartimageagain.com)."
        t3 = "This \nis **text** with \nan *italic* word \nand a `code block` and \nan ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        print("Test 1")
        print("------")
        for n in text_to_textnodes(t):
            print(n)
        print("Test 2")
        print("------")
        for n in text_to_textnodes(t2):
            print(n)

        print("Test 3")
        print("------")
        for n in text_to_textnodes(t3):
            print(n)

if __name__ == "__main__":
    unittest.main()