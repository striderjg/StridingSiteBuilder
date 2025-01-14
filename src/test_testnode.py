#!/usr/bin/env python3

import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noeq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, url="https://www.fakeurl.com")
        self.assertNotEqual(node, node2)
        node2.text_type = TextType.BOLD
        node2.url = None
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()