class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)

        for c in a:
            if b[c]<a[c]: return False
        return True