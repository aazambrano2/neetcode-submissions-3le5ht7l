class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for n in nums:
            if n not in dup:
                dup.add(n)
            else:
                return True
        return False

        