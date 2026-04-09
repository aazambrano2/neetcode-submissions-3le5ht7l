class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

    #     p1 = 0
    #     p2 = 1

    #     while p1 < p2:
    #         if numbers[p1] + numbers[p2] == target and p1 != p2:
    #             return [p1+1,p2+1]
    #         elif p1 < p2:
    #             p2 += 1
    #         else:
    #             p1 += 1
            
    #     return []


    # '''
    # Input: numbers = [1,2,3,4], target = 3
    # p1=0
    # p2=1
    # t=3
    

    # Output: [1,2]
    # '''

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

        