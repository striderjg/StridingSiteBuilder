from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if(not self.tag):
            raise ValueError(f"ParentNode.to_html - {self} - missing tag")
        if(not self.children):
            raise ValueError(f"ParentNode.to_html - {self} - missing children")
        
        html_str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_str = html_str + child.to_html()
        html_str = html_str + f"</{self.tag}>"
        return html_str