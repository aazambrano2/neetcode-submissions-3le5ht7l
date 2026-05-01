class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        # sort by frequency descending after creating counter
        sorted_count = sorted(num_count, key=num_count.get, reverse=True)
        return sorted_count[:k]