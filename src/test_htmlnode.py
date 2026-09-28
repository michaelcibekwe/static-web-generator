import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node2.props_to_html())
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_p(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
if __name__ == "__main__":
    unittest.main()