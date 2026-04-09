class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        """
        
        """

        if len(nums) == 0: return False

        dup = set()

        for n in nums:
            if n not in dup:
                dup.add(n)
            else:
                return True
        return len(nums) != len(set(nums))
        #return False
        