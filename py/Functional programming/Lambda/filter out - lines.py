def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter(lambda word: not word.startswith("-"), document.split("\n")))