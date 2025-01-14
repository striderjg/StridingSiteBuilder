import unittest
from textnode import TextNode, TextType, split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic(self):
        print("==================== Doing normal tests ===================")
        text_italic_node_lst = [ 
            TextNode("This is a string with *a single* delimiter", TextType.NORMAL),
            TextNode("*Italic* is the first word", TextType.NORMAL),
            TextNode("This sentences last word is in *italic*", TextType.NORMAL),
            ]
        text_bold_node_lst = [
            TextNode("This is a **bold** test", TextType.NORMAL),
            TextNode("**This** is a bold first word", TextType.NORMAL),
            TextNode("This is a sentance with the last word **bold**", TextType.NORMAL )
        ]

        returned_lst = split_nodes_delimiter(text_bold_node_lst, "**", TextType.BOLD)
        returned_lst = split_nodes_delimiter( returned_lst + text_italic_node_lst, "*", TextType.ITALIC)


        for i in returned_lst:
            print(i)

    def test_specialCases(self):
        print(" ========== Doing Special Case Test =============")
        text_multiple_bold_delims =  [
            TextNode("This **bold** string has many **bold** statments", TextType.NORMAL),
            TextNode("**Bold** is the way to be **bold**", TextType.NORMAL)
        ]

        returned_lst = split_nodes_delimiter(text_multiple_bold_delims, "**", TextType.BOLD)

        for i in returned_lst:
            print(i)

    def test_emptyString(self):
        print(" ================ Testing Empty String=====================")
        rl = split_nodes_delimiter([TextNode("", None)], "*", TextType.BOLD)
        for i in rl:
            print(i)

    def test_exceptions(self):
        print(" ====================== Testing Exceptions ======================")
        try:
            rl = split_nodes_delimiter( [TextNode("This *string has a unterminated delimiter", None)], "*", None)
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    unittest.main()
