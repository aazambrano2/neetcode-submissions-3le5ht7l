class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        Input: s = "Hello World"

        Output: 5
        '''
        # length = 0

        # for i in range(len(s)-1, -1 , -1):
        #     if s[i] != ' ':
        #         length+=1
        #     else:
        #         return length
        
        # return 0

        return len(s.split().pop())