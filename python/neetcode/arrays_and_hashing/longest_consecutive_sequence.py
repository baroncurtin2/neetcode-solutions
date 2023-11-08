def longest_consecutive(nums: list[int]) -> int:
    """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    Args:
        nums (list[int]): list of numbers

    Returns:
        int: _description_
    """
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        # skip current number who has a number that comes before them in the set b/c
        # the current number can't be the starting point
        if num - 1 in nums_set:
            continue

        count = 0

        while num + count in nums_set:
            count += 1
        longest = max(longest, count)
    return longest