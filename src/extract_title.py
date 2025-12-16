from markdown_to_blocks import markdown_to_blocks


def extract_title(md: str):
    blocks = markdown_to_blocks(md)
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise Exception("not title found")
