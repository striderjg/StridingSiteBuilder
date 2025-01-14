import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic(self):
        l1 = LeafNode("I", "Italic 1")
        l2 = LeafNode("B", "Bold 1")
        l3 = LeafNode(None, "Plain Text 1")
        l4 = LeafNode("A", "Link 1", {"href":"http://linky.com"})

        p1 = ParentNode("P", [l1,l3,l2,l4])
        ul1 = ParentNode("UL", [l3, l2, l4])
        p2 = ParentNode("P", [ul1, l1])
        t3 = ParentNode("OL", [l1])
        t4 = ParentNode("P", None)
        t5 = ParentNode(None, [l1])
        t6 = ParentNode("P", [l1], {"FakePropery":"IAmAFakeProp"})
        print(p1.to_html())
        print("")
        print(p2.to_html())
        print(t3.to_html())
        print(t6.to_html())
        
        try:
            print(t4.to_html())
        except ValueError as e:
            print(e)
        try:
            print(t5.to_html())
        except ValueError as e:
            print(e)

        print("End")
if __name__ == "__main__":
    unittest.main()