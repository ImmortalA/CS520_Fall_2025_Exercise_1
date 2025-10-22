def is_palindrome(s: str) -> bool:
    # BUG: Does not ignore non-alphanumeric characters or case
    return s == s[::-1]


