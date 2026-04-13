class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
#T: nlogn tim sort
#S: O(1) or O(n) worst case

        