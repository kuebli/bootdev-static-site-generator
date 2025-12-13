import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Test LeafNode")
        self.assertEqual(node.to_html(), "<p>Test LeafNode</p>")

    def test_leaf_to_tmll_a(self):
        node = LeafNode("a", "Link", {"href": "www.google.ch", "target": "_blank"})
        html = '<a href="www.google.ch" target="_blank">Link</a>'
        self.assertEqual(node.to_html(), html)

    def test_leaf_to_tmll_div(self):
        node = LeafNode("div", "Test div", {"class": "text-red-200"})
        html = '<div class="text-red-200">Test div</div>'
        self.assertEqual(node.to_html(), html)


if __name__ == "__main__":
    unittest.main()
