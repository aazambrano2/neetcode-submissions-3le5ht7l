class Solution:
    '''
    given int array nums

    return triplets [[nums[i],nums[j], nums[k]]]

    where the sum of the elements are 0 and the indicies are distinct

    NO DUPLICATE TRIPLES and return in any order


    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]

    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].

    validator = 0

    nums = [-1,0,1,2,-1,-4]

    0 + -1 = -1 record index
    -1 + 0 = -1 record index
    1 + -1 = 0 record index

    move on to next possible combination

    0+1=1 record index
    1+1=2 record index
    2+2=4 record index

    not valid but move the third one


    [0,1,2]

    if all three sum to 0 : add to answer array

    tiplet = [-1,0,1] Y | 


    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            


        