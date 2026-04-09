from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Input: s = "racecar", t = "carrace"
        racecar

        carrace

        
            '''
        if len(s) == 0 or len(t) == 0:
            return False
        
        if len(s) != len(t):
            return False
        
        return Counter(s.lower()) == Counter(t.lower())

        # for c in s:
        #     if c not in t:

        #         return False
        # return True


       