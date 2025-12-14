import unittest
from extract_markdown_links import extract_markdown_links


class TestExtractMarkdornLinks(unittest.TestCase):
    def test_one_link_end(self):
        text = "This is text with a link: [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_links(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
