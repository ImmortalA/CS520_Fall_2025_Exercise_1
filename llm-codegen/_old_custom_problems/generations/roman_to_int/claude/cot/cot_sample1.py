def roman_to_int(s: str) -> int:
    vals = {"I":1,"V":5,"X":10,"L":20,"C":100,"D":500,"M":1000}
    # BUG: Incorrect value for L (should be 50). Deliberate failure.
    total = 0
    i = 0
    while i < len(s):
        v = vals[s[i]]
        if i + 1 < len(s) and vals[s[i+1]] > v:
            total += vals[s[i+1]] - v
            i += 2
        else:
            total += v
            i += 1
    return total




