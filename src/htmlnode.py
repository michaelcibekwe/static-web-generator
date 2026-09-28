class HTMLNode:
    def __init__(self, tag=None, value=None, children:list[HTMLNode]=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        result = ""
        if self.props == None:
            return result
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __repr__(self):
        print(f"Tags: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Children: {self.children}")
        print(f"Props: {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props:dict=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value detected")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children:list[HTMLNode], props:dict= None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag found")
        if self.children == None:
            raise ValueError("No children found")
        result = f"<{self.tag}>"
        for node in self.children:
            if isinstance(node, LeafNode) or isinstance(node, ParentNode):
                result += node.to_html()
        result += f"</{self.tag}>"
        return result