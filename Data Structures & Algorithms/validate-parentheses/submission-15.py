class Solution:

    #stack/ queue solution

    '''

    given string s with possible characters ( ) {} []


    s is valid iff

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    return True if s is valid else false

    use a stack

    ([{}])

    [(] -> [([{] -> [([{] -> [([)] or [([](]

    t       t        t    then false

    '''
    def isValid(self, s: str) -> bool:

        stack = []
        
        i = 0

        dictionary = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        while i != len(s):
            if s[i] not in dictionary:
                stack.append(s[i])
                i += 1
                continue

            if  not stack or stack[-1] != dictionary[s[i]]:
                return False
            stack.pop()
            i += 1
            # print(stack)
            
        return not stack
        
        

            
            


        