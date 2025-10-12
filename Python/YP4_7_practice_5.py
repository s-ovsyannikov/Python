from typing import List, Dict


def count_frequencies(words: List[str]) -> Dict[str, int]:
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result
