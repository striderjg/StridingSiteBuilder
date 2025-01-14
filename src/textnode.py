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
    



