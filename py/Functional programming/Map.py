def change_bullet_style(document: str) -> str:
    split_doc = document.split("\n")
    translated_doc = map(convert_line, split_doc)
    rejoin_doc = "\n".join(translated_doc)
    return rejoin_doc

#optimised:     return "\n".join(map(convert_line, document.split("\n")))
# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
