from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Args:
        s (str): string 1
        t (str): string 2

    Returns:
        bool: True if anagram, else False
    """
    if len(s) != len(t):
        return False

    counter = defaultdict(int)

    for i in range(len(s)):
        counter[s[i]] += 1
        counter[t[i]] -= 1

    return all(x == 0 for x in counter.values())
