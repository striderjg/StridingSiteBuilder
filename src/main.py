#!/usr/bin/env python3
from textnode import *
from leafnode import LeafNode
from shutil import rmtree, copy
from webgen import WebGen
import os
import re

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

def main():
    tree_copy(STATIC_DIR, GENERATED_DIR)
    wg = WebGen()
    out_path = os.path.join(GENERATED_DIR, "index.html")
    wg.generate_page("content/index.md", "template.html", out_path)
    

if __name__ == "__main__":
    main()