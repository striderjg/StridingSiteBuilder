#!/usr/bin/env python3
from textnode import *
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("B", text_node.text)
        case TextType.ITALIC:
            return LeafNode("I", text_node.text)
        case TextType.CODE:
            return LeafNode("CODE", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError(f"None existent TextType")

def italic_to_html_node(node):
    return

def code_to_html_node(node):
    return

def link_to_html_node(node):
    return

def image_to_html_node(node):
    return

def main():
    dummy = TextNode("This is a dumb text node", TextType.CODE)
    print(dummy)



if __name__ == "__main__":
    main()