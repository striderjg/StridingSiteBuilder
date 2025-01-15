import unittest
from webgen import WebGen

class TestBlockToBlockType(unittest.TestCase):
    def test_basic(self):
        test_cases = [
            ("# Heading 1\n## Heading 2\n#### Heading 4", "heading"),
            ("```\nA code\nblock of \nmultiple lines\n```", "code"),
            ("> a quote\n>block\n> > with a few quotes\n> here", "quote"),
            ("* list item\n- also a list item\n* another list item", "unordered_list"),
            ("1. item 1\n2. item 2\n3. item 3", "ordered_list"),
            ("1. a malformed\n1. ordered list", "paragraph")
        ]
        print("============= Doing basic block_to_block_type(block) tests ==============")
        for tstr, type in test_cases:
            if WebGen.block_to_block_type(tstr) == type:
                print(f"{tstr} : {type} -> passed\n")
            else:
                print(f"{tstr} : {type} -> failed\n")


if __name__ == "__main__":
    unittest.main()