from collections import defaultdict


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = defaultdict(int)

    for n in nums:
        counter[n] += 1

    sorted_nums_per_freq = [
        k for k, v in sorted(counter.items(), key=lambda item: -item[1])
    ]
    return sorted_nums_per_freq[:k]
