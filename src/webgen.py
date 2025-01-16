import re
from parentnode import ParentNode
from textnode import TextNode, TextType, text_to_textnodes
from leafnode import LeafNode
from htmlnode import HTMLNode

class WebGen:
    def __init__(self):
        self.html_head = ParentNode("div", None)

    # Desc:     WebGen method.  Takes a string containing markdown formated text and constructs
    # Desc:     a tree of HTMLNodes as attribute of WebGen
    # IN:       A string containing a markdown formated text
    # OUT:      Populates head with a tree of 
    # TODO:  Fininsh
    def markdown_to_html_node(self, markdown):
        blocks_lst = WebGen.markdown_to_blocks(markdown)
        #print(blocks_lst)
        html_nodes_list = []
        for block in blocks_lst:
            block_html_node = self.__block_to_html(block)
            html_nodes_list.append(block_html_node)
        return html_nodes_list
    # Helper Funcs for markdown_to_html_ndoe
    
    # Desc:     takes a string containing a block of markup text and returns a tree of htmlnodes
    # IN:       block -> string -> markuptext
    # OUT:      HTMLNode contianing converted markup
    def __block_to_html(self, block):
        block_type = WebGen.block_to_block_type(block)
        #lines = block.split("\n")
        block_text_nodes = []
        block_html_node_head = []
        match block_type:
            case "paragraph":
                block_text_nodes = text_to_textnodes(block)
                block_html_node_head = ParentNode(
                    "P",
                    list( map(
                        lambda n: n.to_html_node(), block_text_nodes
                    )),
                    None
                )
            case "heading":
                h_tag = f"H{len( re.match(r"^#{1,6}\s", block).group() ) - 1}"

                block = re.sub(r"^#{1,6}\s","", block)
                block_text_nodes = text_to_textnodes(block)
                block_html_node_head = ParentNode(
                    h_tag,
                    list( map(
                        lambda n: n.to_html_node(), block_text_nodes
                    )),
                    None
                )
            case "code":
                pass
            case "quote":
                pass
            case "unordered_list":
                pass
            case "ordered_list":
                pass
            case _:
                raise ValueError(f"Unknown block type in {self} - markdown_to_html_node(self, markdown)")
        return block_html_node_head

    # Static method.  Returns a list of strings of markdown 'blocks' - seperated by blank line
    #in:        markdown -> raw markdown document string
    #out:       list of strings containing markdown blocks
    #raises:    ValueError if no markdown passed in
    def markdown_to_blocks(markdown):
        #input checking
        if(not isinstance(markdown, str)):
            raise ValueError(f"markdown_to_blocks expects str.  Recieved: {type(markdown)}")
        lines = markdown.split("\n")
        if(not lines):
            raise ValueError("No markdown text passsed in")
        
        # strip newlines at start of document
        while(not lines[0] ):
            lines.pop(0)
            if(not lines):
                raise ValueError("No markdown text passsed in")
            
        blocks = [""]
        i = 0
        while(lines):
            # A new block
            if(lines[0] == ""):
                blocks[i] = blocks[i][1:] # trim leading \n
                #find next block
                while(lines and not lines[0]):
                    lines.pop(0)
                if(not lines):
                    break
                i += 1
                blocks.append("")

            blocks[i] = blocks[i] + "\n" +  lines[0].strip()
            lines.pop(0)
        blocks[i] = blocks[i][1:]
        return blocks
    
    # Static Method.  Returns string indetifying passed in markup block type
    #in:    block -> A list of strings with no leading or trailing spaces containing a markup block
    #out:   string describing block type
    def block_to_block_type(block):
        funcs_isType = [WebGen.__isHeading, WebGen.__isCode, WebGen.__isQuote, WebGen.__isUnordered, WebGen.__isOrdered]
        for func in funcs_isType:
            r = func(block)
            if(r):
                return r
        return "paragraph"
    

    # Helper funcs for block_to_block_type(block)
    def __isHeading(block):
        if(re.match(r"^#{1,6}\s", block)):
            return "heading"
        return False
    
    def __isCode(block):
        if(re.fullmatch(r"^```.+?```$", block, re.S)):
            return "code"
        return False
    
    def __isQuote(block):
        for line in block.split("\n"):
            if(not line):
                raise ValueError("block_to_block_type recieved a block containined an empty line")
            if line[0] != '>':
                return False
        return "quote"
    
    def __isUnordered(block):
        for line in block.split("\n"):
            if not line:
                raise ValueError("block_to_block_type recieved a block containined an empty line")
            if not re.match(r"^[*-]\s", line):
               return False
        return "unordered_list"
    
    def __isOrdered(block):
        lines = block.split("\n")
        for i in range(0, len(lines)):
            if not lines[i]:
                raise ValueError("block_to_block_type recieved a block containined an empty line")
            
            if(f"{lines[i][0]}. " != f"{i+1}. "):
                return False
        return "ordered_list"
    

    