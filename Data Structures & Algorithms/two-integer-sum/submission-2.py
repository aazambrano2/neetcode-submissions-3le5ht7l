class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [3,4,5,6], target = 7

        Output: [0,1]
        '''

        if len(nums) == 2:
            return [0,1]
        
        calculator = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in calculator:
                return [calculator[complement],i]
            else:
                calculator[nums[i]] = i
        return []
        