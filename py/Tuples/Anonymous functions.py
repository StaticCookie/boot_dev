#Script will return
from collections.abc import Callable

### Example of input
#file_extension_tuples: list[tuple[str, list[str]]] = [
#    ("document", [".doc", ".docx"]),
#    ("image", [".jpg", ".png"])
#]
# resulting dictionary

### Example of output
#file_extensions_dict: dict[str, str] = {
#    ".doc": "document",
#    ".docx": "document",
#    ".jpg": "image",
#    ".png": "image",
#}

def file_type_getter(
        file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:

    file_dict = {}

    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_dict[ext] = tup[0]
    return lambda argument: file_dict.get(argument, "Unknown")