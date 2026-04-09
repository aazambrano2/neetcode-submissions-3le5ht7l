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


       
        


        