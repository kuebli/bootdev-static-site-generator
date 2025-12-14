import re


def extract_markdown_links(text: str):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links_found = re.findall(pattern, text)
    return links_found
