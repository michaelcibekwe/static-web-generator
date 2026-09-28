import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        test1 = HTMLNode(None, None, None, None)
        # print(test1)
        print(test1.props_to_html())
    def test_only_dict(self):
        test2 = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        # print(test2)
        print(test2.props_to_html())
    def test_no_dict(self):
        test3 = HTMLNode("a", "The Fitness Gram Pacer Test", None, {"href": "https://www.google.com"})
        # print(test3)
        print(test3.props_to_html())

if __name__ == "__main__":
    unittest.main()