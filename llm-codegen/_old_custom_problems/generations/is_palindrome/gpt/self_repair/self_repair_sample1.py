def is_palindrome(s: str) -> bool:
    t = [ch.lower() for ch in s if ch.isalnum()]
    return t == t[::-1]


