from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, txt, txt_type, url=None):
        self.text, self.text_type, self.url = txt, txt_type, url

    def __eq__(self, b):
        return self.text == b.text and self.text_type == b.text_type and self.url == b.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
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