class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # nums.sort()
        # ans = []
        # count = Counter(nums)
        
        # ans.append(nums[len(nums)//3])
        # nums = [x for x in nums if x != ans[-1]]
        
        
        # if len(nums) <= 1:
        #     return ans
        # elif len(set(count.values())) == 1:
        #     return []
        # else:
        #      ans.append(nums[len(nums)//3])

        # return ans
        count = Counter(nums)
        res = []

        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)

        return res

        