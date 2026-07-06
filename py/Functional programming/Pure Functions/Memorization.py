## Functions check if data is stored already to utilize RAM over CPU use.

def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    clone = memos.copy()
    if document in clone:
        return clone[document], clone
    else:
        clone[document] = word_count(document)
        return clone[document], clone

def word_count(document: str) -> int:
    count = len(document.split())
    return count
