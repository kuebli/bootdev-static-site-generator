import re


def extract_markdown_images(text: str):
    images_found = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return images_found
