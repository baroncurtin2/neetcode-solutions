from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Given an array of strings strs, groups the anagrams together.

    Args:
        strs (list[str]): array of strings

    Returns:
        list[list[str]]: list of grouped anagrams
    """
    grouper = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        grouper[sorted_word].append(word)

    return list(grouper.values())
