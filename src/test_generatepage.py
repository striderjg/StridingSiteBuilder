import unittest
from webgen import WebGen

class TestGeneratePage(unittest.TestCase):
    def test_basic(self):
        fname_mu = "content/index.md"
        fname_tp = "template.html"
        fname_out = "public"

        #webgen_obj = WebGen()
        #webgen_obj.generate_page(fname_mu, fname_tp, fname_out)

if __name__ == "__main__":
    unittest.main()