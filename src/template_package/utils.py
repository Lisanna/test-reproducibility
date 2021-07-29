from typing import List, Tuple


def iter_together(path_1: str, path_2: str) -> List[Tuple[str, str]]:
    """Open two files and iterate over them together.

    :param path_1: The file path of the left file
    :param path_2: The file path of the right file
    :returns: Pairs of lines for the two files
    """
    with open(path_1) as file_1, open(path_2) as file_2:
        results = []
        for line_1, line_2 in zip(file_1, file_2):
            results.append((line_1, line_2))
    return results
