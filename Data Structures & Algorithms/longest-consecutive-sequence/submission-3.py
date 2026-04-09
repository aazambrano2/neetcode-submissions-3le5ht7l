class Solution:
    '''
    Given nums
    return length of longest consecutive sequence

    Input: nums = [0,3,2,5,4,6,1,1] output = 7

    we can sort the array and check difference of each number no greater than 1

    But we keep in mind that run time must be O(n)
    
    Get length

    len = 8

    why dont we go front and back?

    set(0,3,2,5,4,6,1) Find 1?

    current = 0 / 1 / 

    if your next n is in set:
        update current
        iterate finding your next number until no more
    
    '''
    def longestConsecutive(self, nums: List[int]) -> int:

        
        checker = set(nums)

        consecutive = 0

        for n in checker:
           
            if n - 1 not in checker:
                length = 1
                while n + length in checker:
                        length += 1
                consecutive = max(length,consecutive)
        
        return consecutive
                




        