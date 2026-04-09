class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    #     if set(s).issubset(set(t)): 
    #         return True
        l = 0   # pointer for s
        r = 0   # pointer for t

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1   # move s pointer only on match
            r += 1       # always move t pointer

        return l == len(s)   # True if we matched all of s
       
            