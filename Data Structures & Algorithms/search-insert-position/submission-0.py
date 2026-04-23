class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1

        
        ans = len(nums)
        while l <= r:
            location = l + ((r - l) // 2) #overflow solution
            if nums[location] > target:
                #scope is now towards the left of the array
                ans = location
                r = location - 1
            elif nums[location] < target:
                #scope is now towards the right of the array
                l = location + 1
            else:
                return location
        
        return ans