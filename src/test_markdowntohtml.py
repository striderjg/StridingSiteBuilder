import unittest
from webgen import WebGen
from htmlnode import HTMLNode

class TestMarkdownToHtml(unittest.TestCase):
    def test_basic(self):
        print("==================== Doing basic WebGen.markdown_to_html(text) tests ================")
        web_obj = WebGen()
        t = "A two line paragraph\na second line\n\nA second paragraph"
        test_cases = [
            "# A level 1 heading",
            "### A level 3 heading",
            "A two line paragraph\na second line\n\nA second paragraph",
            "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        ]

        b = WebGen.markdown_to_blocks(t)
        for test in test_cases:
            ret = web_obj.markdown_to_html_node(test)
            for node in ret:
                print(node.to_html())

        '''
        ret = web_obj.markdown_to_html_node(t)
        print(ret)
        for node in ret:
            print(node.to_html())
        '''

if __name__ == "__main__":
    unittest.main()        
