def two_sum(nums: list[int], target: int) -> list[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

    Args:
        nums (list[int]): list of numbers
        target (int): target for sum

    Returns:
        list[int]: pair of numbers adding to target
    """
    indices = {}

    for i, num in enumerate(nums):
        if num in indices:
            return i, indices[num]

        indices[target - num] = i
