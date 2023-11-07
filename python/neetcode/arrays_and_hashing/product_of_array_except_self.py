def product_except_self(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]

    Args:
        nums (list[int]): list of numbers

    Returns:
        list[int]: array where each items is the product of all the elements except the original element at that index
    """
    n = len(nums)
    result = [1] * len(nums)
    prefix = 1
    postfix = 1

    for i in range(n):
        result[i] *= prefix
        result[n - 1 - i] *= postfix

        prefix *= nums[i]
        postfix *= nums[n - 1 - i]

    return result
