class Solution:
    '''
    Given s -> upper case, 
    int k
    replace any character k iff its upercase
        

        Input: s = "AAABABB", k = 1

        A A A B A B B
          |         |
          l         r
        
        dictionary = {A: 4
        B: 3 } 
        Output: 5

    '''
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        char_couter = dict()
        answer = 0
        maximum = 0

        for r in range(len(s)):
            char_couter[s[r]] = 1 + char_couter.get(s[r],0) 
            maximum = max(maximum,char_couter[s[r]])

            
            if (r - l + 1) - maximum > k:
                char_couter[s[l]] -= 1
                l += 1

        return (r - l + 1)

        