class HTMLNode:
    def __init__(self, tag=None, value=None, children:list[HTMLNode]=None, props:dict = {"key": "value"}):
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
