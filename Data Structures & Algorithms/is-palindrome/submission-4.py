import re
class Solution:

    '''
    given string s

    return if palidorme, else false
    '''
    def isPalindrome(self, s: str) -> bool:

        #two pointers

        s = s.replace(" ", "")
        s = s.strip()
        #re expressions are cooler
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        l = 0
        r = len(s)-1
        for i in range(len(s)):
            if s[l] != s[r]:
                return False
            if l > r:
                break
            l = l + 1
            r = r - 1
        return True

    '''
    s = wasitacaroracatisaw
    '''
        