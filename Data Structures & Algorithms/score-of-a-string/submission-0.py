class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        Input: s = "code"

        Output: 24
        Explanation: The ASCII values of the characters in the given string are: 'c' = 99, 'o' = 111, 'd' = 100, and 'e' = 101. The score of s will be: |111 - 99| + |100 - 111| + |101 - 100|.
        
        '''
        if len(s) == 2:
            return abs(ord(s[1])-ord(s[0]))
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i+1])-ord(s[i]))
        return sum


        