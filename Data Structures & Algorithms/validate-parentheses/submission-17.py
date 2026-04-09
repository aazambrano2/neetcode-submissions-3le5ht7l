class Solution:
    def isValid(self, s: str) -> bool:
        # checker = {'(':')','{':'}','[':']'}
        
        # l = 0
        # r = len(s) - 1

        # while l < r:
        #     if checker[s[l]] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True


        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        



        