class Solution:
    '''

    Input: s = "zxyzxyz"
                   l  r
    

   use a set to keep track of duplicates as well


    Output: 3

    '''
    def lengthOfLongestSubstring(self, s: str) -> int:

        duplicates = set()
        l = 0
        answer = 0

        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1
            duplicates.add(s[r])
            answer = max(answer, r - l + 1)
        return answer
        