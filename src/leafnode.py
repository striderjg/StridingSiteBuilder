from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.tag:
            return self.value
        
        ret_str = ""
        ret_str =  f"<{self.tag}{self.props_to_html()}>"
        if(self.value):
            ret_str = ret_str + self.value
        if(self.tag.casefold() != "img"):
            ret_str = ret_str + f"</{self.tag}>"
        return ret_str