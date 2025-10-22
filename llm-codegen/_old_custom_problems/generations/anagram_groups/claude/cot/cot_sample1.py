from typing import List, Dict


def anagram_groups(words: List[str]) -> List[List[str]]:
    groups: Dict[str, List[str]] = {}
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


