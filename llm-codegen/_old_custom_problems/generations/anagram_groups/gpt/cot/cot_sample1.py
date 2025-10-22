def anagram_groups(words: list[str]) -> list[list[str]]:
    from collections import defaultdict
    groups: dict[tuple, list[str]] = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())




