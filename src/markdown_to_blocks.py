def markdown_to_blocks(document: str):
    blocks = map(lambda t: t.strip(), document.split("\n\n"))
    return list(filter(lambda b: len(b) > 0, blocks))
