import unittest
from extract_markdown_images import extract_markdown_images


class TestExtractMarkdornImages(unittest.TestCase):
    def test_one_link_end(self):
        text = "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_images(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(result, expected)

    def test_multiple_links(self):
        text = "This is text with an image ![to boot dev](https://www.boot.dev)"
        result = extract_markdown_images(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
        ]
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
