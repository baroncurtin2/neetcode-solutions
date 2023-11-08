def two_sum(numbers: list[int], target: int) -> list[int]:
    """Returns the indices of the two elements whose sum adds to the target

    Args:
        numbers (list[int]): list of numbers
        target (int): target sum

    Returns:
        list[int]: indices of the two elements whose sum adds to the target
    """
    start, end = 0, len(numbers) - 1

    while start < end:
        num_sum = sum([numbers[start], numbers[end]])
        if num_sum == target:
            return [start + 1, end + 1]
        elif num_sum < target:
            start += 1
        elif num_sum > target:
            end -= 1