import unittest
from webgen import WebGen

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic(self):
        s = "\n\n\n\nfirst block\n\n     Second block\nSecond block line 2         \nSecond block line 3\n\nThird block\n"
        
        ret = WebGen.markdown_to_blocks(s)

        print(type(ret))

        for i in range(0,len(ret)):
            print(f"Start {i}:================================")
            print(f"{ret[i]}")
            print(f"End {i}:================================")
    
if __name__ == "__main__":
    unittest.main()