class Solution:

    def search(self, nums: List[int], target: int) -> int:

        #have two pointers:

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            #formula to update location
            location = l + ((r - l) // 2)
            
            if nums[location] > target:
                r = location - 1

            elif nums[location] < target:
                l = location + 1
                
            else:
                return location
        
        return -1
        



        
'''

nums array sorted ascending order

you have an int target

implement a function to search for target

return index otherwise return -1

O(logn) time complexity

example:

Input: nums = [-1,0,2,4,6,8], target = 1

[-1,1,2,2,2,4,4,5,4] start in the middle

i = (len(nums) / 2

if n[i] < target:
    i = i / 2
    
if n[i] > target:
    i = len(nums) - i

if nums[i] == target:
    return i


Output: -1
'''


        