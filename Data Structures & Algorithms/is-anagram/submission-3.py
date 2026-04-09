from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        Input: s = "racecar", t = "carrace"
        racecar

        carrace

        T: O(N) S: O(N)
    
        
            '''
        if len(s) == 0 or len(t) == 0:
            return False
        
        if len(s) != len(t):
            return False
        
        return Counter(s.lower()) == Counter(t.lower())

# def is_anagram(s1, s2):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     s1, s2 = s1.lower(), s2.lower()
#     return all(s1.count(c) == s2.count(c) for c in alphabet) this is how you do it with S: O(1)


       