class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Input: nums = [1,2,4,6]

        Output: [48,24,12,8]

        48 = 2 * 4 * 6

        visit each i element

        save the product of non i elements

        continue

        
        '''


        
        prefix = [1]
        suffix = [1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        print(prefix)

        for i in range(len(nums)-1,0,-1):
            print(i)
            suffix.append(suffix[-1]*nums[i])
        suffix = suffix[::-1]
        print(suffix)


        return [prefix[i]*suffix[i] for i in range(len(nums))]

        
