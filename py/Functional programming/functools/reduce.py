import functools


def join(doc_so_far: str, sentence: str) -> str:
    #print(f"doc so far: {doc_so_far}, sentence: {sentence}")
    return f"{doc_so_far}. {sentence}"


def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0:
        return ""

    combined =  functools.reduce(join, sentences[:n])
    return f"{combined}."