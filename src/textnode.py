from enum import Enum
import re

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text, self.text_type, self.url = text, text_type, url

    def __eq__(self, b):
        return self.text == b.text and self.text_type == b.text_type and self.url == b.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_to_textnodes(text):
    lst_nodes = [TextNode(text, TextType.NORMAL)]
    
    lst_nodes = split_nodes_delimiter(lst_nodes, "**", TextType.BOLD)
    lst_nodes = split_nodes_delimiter(lst_nodes, "*", TextType.ITALIC)
    lst_nodes = split_nodes_delimiter(lst_nodes, "`", TextType.CODE)
    lst_nodes = split_nodes_image(lst_nodes)
    lst_nodes = split_nodes_link(lst_nodes)

    return lst_nodes
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if( not n.text or len(n.text) == 0):
            continue

        text = n.text
        start_index = text.find(delimiter)
        while(start_index >= 0):
            if(start_index != 0):
                pre_node = TextNode(text[:start_index], n.text_type, n.url)
                new_nodes.append(pre_node)

            end_index = text.find(delimiter, start_index+len(delimiter))
            if(end_index < 0):
                raise Exception("Unterminated delimiter")

            new_node = TextNode(text[start_index+len(delimiter):end_index], text_type, n.url)
            new_nodes.append( new_node )

            if(end_index < len(text) - len(delimiter)):
                text = text[end_index+len(delimiter):]
            else:
                text = ""
            start_index = text.find(delimiter)

        if(len(text) > 0):
            new_nodes.append(
                TextNode(text, n.text_type, n.url)
            )
    return new_nodes

def extract_markdown_images(text):
    alt_text_lst = re.findall(r"(?:!\[)([^\]]*?)(?:\]\(.*?\))", text)
    img_link_lst = re.findall(r"(?:!\[[^\]]*?\]\()([^\)]*?)(?:\))", text)
    if(len(alt_text_lst) != len(img_link_lst)):
        raise Exception("Found unequal links vs alt texts")
    
    return list(zip(alt_text_lst, img_link_lst))

def extract_markdown_links(text):
    alt_text_lst = re.findall(r"(?:\[)([^\]]*?)(?:\]\(.*?\))", text)
    img_link_lst = re.findall(r"(?:\[[^\]]*?\]\()([^\)]*?)(?:\))", text)

    if(len(alt_text_lst) != len(img_link_lst)):
        raise Exception("Found unequal links vs alt texts")
    
    return list(zip(alt_text_lst, img_link_lst))

# in:   list of TextNode
# out:  list of TextNodes split by inline image markup   
def split_nodes_image(old_nodes):
    return __split_nodes_image_link(extract_markdown_images, old_nodes, "![")

# in:   list of TextNode
# out:  list of TextNodes split by inline image markup   
def split_nodes_link(old_nodes):
    return __split_nodes_image_link(extract_markdown_links, old_nodes, "[")

# in:   Function to extract elements,  list of TextNode, characters to start split
# out:  list of TextNodes split by inline link markup   
def __split_nodes_image_link(extract_func, old_nodes, start_delim):
    new_nodes = []
    
    # for every TextNode passed in
    for n in old_nodes:
        if( not n.text or len(n.text) == 0):
            continue

        text = n.text
        images_lst = extract_func(text)
        
        # For every image tag
        for alt_txt, link in images_lst:
            pre_text, post_text = text.split(f"{start_delim}{alt_txt}]({link})", 1)
            if(len(pre_text) > 0):
                new_nodes.append( TextNode(pre_text, n.text_type, n.url) )

            # construct and append the image node
            new_nodes.append( TextNode(alt_txt, TextType.IMAGE, link) )

            # Keep working on remaining text
            text = post_text
        # deal with remainder of line
        if(len(text) > 0):
            new_nodes.append( TextNode(text, n.text_type, n.url))
    # Done looping through old_nodes                            
    return new_nodes