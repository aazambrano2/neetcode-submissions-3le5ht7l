from collections import Counter


class Solution:

    '''
    we can use the collection class to get the frequent amount of elements in a list

    o(n)

    [1,2,2,3,3,3] k = 1

    answer = [3]

    get the next max number of frequency by element until k = 0

    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = Counter(nums).most_common()

        max_n = 0
        ans = []
        for f in frequency:
            ans.append(f[0])
            k -= 1
            if k == 0:
                break
        return ans    