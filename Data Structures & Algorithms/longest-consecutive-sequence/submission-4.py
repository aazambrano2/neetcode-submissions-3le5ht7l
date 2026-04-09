class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,20,4,10,3,4,5]

        Output: 4

        set to find all consecutive sequence for each i element

        you could have two pointers to only inlcude i elements that have a difference of 1


        '''

        # if len(nums) == 0:
        #     return 0

        # left = 0
        # right = len(nums) - 1
        # lset, rset = set(), set()
        # while left < right:
        #     lset.add(nums[left])
        #     rset.add(nums[right])
        #     left += 1
        #     right -= 1
        # if left == right:
        #     lset.add(nums[left])

        
        # print(lset,rset)
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        