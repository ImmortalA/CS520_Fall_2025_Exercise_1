from typing import Any


def uniq_in_order(items: list[Any]) -> list[Any]:
    if not items:
        return []
    out = [items[0]]
    for x in items[1:]:
        if x != out[-1]:
            out.append(x)
    return out




