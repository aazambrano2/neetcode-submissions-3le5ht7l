class Solution:
    '''
    Input: nums = [1,2,3]

    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


    recursion and list stripping



    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:

        answer = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                answer.append(subset.copy())
                return
            #decision to include the subset at nums[i] (left branch)
            subset.append(nums[i])
            dfs(i + 1)

            #not to include the subset at nums[i] (right branch)
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return answer
            

    
   




        