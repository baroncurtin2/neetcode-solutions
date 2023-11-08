

from collections import Counter
from itertools import product


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the given list of integers that sum up to zero.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        list[list[int]]: A list of lists, where each inner list represents a unique triplet that sums up to zero.

    """
    if len(nums) < 3:
        return []

    counter = Counter(nums)
    num_set = list(counter.keys())
    triplets = set()

    if counter[0] >= 3:
        triplets.add((0, 0, 0))

    triplets |= find_triplets(counter, num_set)

    return list(triplets)


def find_triplets(counter: Counter, num_set: list[int]) -> set:
    """
    Finds triplets in the given num_set that sum up to zero.

    Args:
        counter (Counter): A Counter object that stores the count of each number in num_set.
        num_set (list[int]): A list of integers.

    Returns:
        set: A set of tuples, where each tuple represents a triplet that sums up to zero.

    """
    positives = [n for n in num_set if n > 0]
    negatives = [n for n in num_set if n < 0]

    triplets = set()

    for n, p in product(negatives, positives):
        target = -(n + p)

        if target in counter and (target not in [n, p] or counter[target] > 1):
            triplets.add(tuple(sorted([p, n, target])))

    return triplets
