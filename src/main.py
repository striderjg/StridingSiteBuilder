#!/usr/bin/env python3
from textnode import *
from leafnode import LeafNode
from shutil import rmtree, copy
import os

GENERATED_DIR = "public"
STATIC_DIR = "static"

def tree_copy(src, dest):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)
    os.chdir("..")

    if not os.path.exists(src):
        raise ValueError("tree_copy(src, dest) was passed an invalid path")   
    
    if( os.path.exists(dest)):
        rmtree(dest)
    os.mkdir(dest)

    __r_copy(src, dest)   
    return

def __r_copy(src, dest):
    src_dir_path = os.path.join(os.getcwd(), src)
    dir_contents = os.listdir(src)
    for content in dir_contents:
        content_path = os.path.join(src_dir_path, content)
        if os.path.isfile(content_path):
            copy(content_path, dest)
        elif os.path.isdir(content_path):
            new_dir = os.path.join(dest, content)
            os.mkdir(new_dir)
            __r_copy(content_path, new_dir)
            
            


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
    tree_copy(STATIC_DIR, GENERATED_DIR)



if __name__ == "__main__":
    main()