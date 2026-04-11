class Solution:
    from collections import Counter
    def removeElement(self, nums: List[int], val: int) -> int:
    #     collect = []
    #     l,r = 0, len(nums) -1

    #     while l < r:
    #         if nums[l] != val:
    #             collect.append(nums[l])
    #         if nums[r] != val:
    #             collect.append(nums[r])
    #         l += 1
    #         r -= 1
    #     return len(collect)
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]  # overwrite in place
                l += 1

        return l



    
                
            
        


        