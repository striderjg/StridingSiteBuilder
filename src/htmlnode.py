class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag, self.value, self.children, self.props = tag, value, children, props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if(not self.props):
            return ""
        ret_str = ""
        for prop in self.props:
            ret_str = ret_str + f" {prop}=\"{self.props[prop]}\""
        return ret_str
    
    def __repr__(self):
        return f"{{{self.tag}, {self.value}, {self.children}, {self.props}}}"