from typing import List, Any


def uniq_in_order(items: List[Any]) -> List[Any]:
    if not items:
        return []
    result = [items[0]]
    for x in items[1:]:
        if x != result[-1]:
            result.append(x)
    return result


