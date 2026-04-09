from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Input: nums = [1,2,2,3,3,3], k = 2

        Output: [2,3]
        '''
        solution = []
        counter_list = Counter(nums)
        solution = sorted(counter_list)
        solution = counter_list.most_common(k)
        # extract keys and sort by value
        return sorted([item[0] for item in solution])


       
    # class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     arr = []
    #     for num, cnt in count.items():
    #         arr.append([cnt, num])
    #     arr.sort()

    #     res = []
    #     while len(res) < k:
    #         res.append(arr.pop()[1])
    #     return res


        