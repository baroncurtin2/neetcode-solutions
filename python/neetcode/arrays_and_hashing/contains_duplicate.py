def contains_duplicate(nums: list[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

    Args:
        nums (list[int]): list of numbers

    Returns:
        bool: True if nums contains duplicate, else False
    """
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
