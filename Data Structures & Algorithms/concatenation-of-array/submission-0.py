class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Input: nums = [1,4,1,2]

        Output: [1,4,1,2,1,4,1,2]
        '''
        
        nums2 = [n for n in nums ]
        return nums + nums2