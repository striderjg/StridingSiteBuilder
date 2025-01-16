import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic(self):
        test_cases = [
            "# Simple search",
            "a harder\ncase\n>with other stuff\n## including other headings\n# and finally what we want",
            "## a second heading\n#A facking heading 1\n###### a 6 heading\n# A real 1st heading\nsome other stuff\n# A second 1st heading"
        ]

        for test in test_cases:
            print(extract_title(test))
            
if __name__ == "__main__":
    unittest.main()