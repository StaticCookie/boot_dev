## Example of a string
doc: str = """I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown."""

## removes all emphasis by calling functions: remove line emphasis and remove word emphasis
def remove_emphasis(doc: str) -> str:
    #global doc
    #lines = doc.split("\n")
    #new_lines = map(remove_line_emphasis, lines)
    #doc = "\n".join(new_lines)
    #return doc
    # Created.a streamlined single line version of code
    return "\n".join(map(remove_line_emphasis, (doc.split("\n"))))

## removes emphasis from each line
def remove_line_emphasis(line: str) -> str:
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)

## Removes word emphasis by removing "*"
def remove_word_emphasis(word: str) -> str:
    return word.strip("*")
