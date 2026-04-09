class Solution:
    '''
    given int nums

    return an array output where output[i] is the product of all elements of nums except nums[i]

    Input: nums = [1,2,4,6]

    Output: [48,24,12,8]

    if i = 0

    product = 2 * 4 * 6

    i = 1

    product = 1 * 4 * 6

    i = 2

    product = 1 * 2 * 6


    how can we do this first and then optimize it?

    use a double loop and get the products

    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 2:
            return [nums[1],nums[0]]
        
        answer = []
        product = 1
        for i in range(len(nums)):
            not_included = i
            for j in range(len(nums)):
                if j == not_included:
                    continue
                else:
                    product = product*nums[j]
            
            
            answer.append(product)
            product = 1
        
        return answer



        