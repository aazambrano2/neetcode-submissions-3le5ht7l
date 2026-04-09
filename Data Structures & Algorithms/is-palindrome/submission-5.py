class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        return cleaned == cleaned[::-1]


        # l, r = 0, len(cleaned) - 1  # ✅ two pointers

        # while l < r:
        #     if cleaned[l] != cleaned[r]:  # ✅ index into cleaned
        #         return False
        #     l += 1
        #     r -= 1

        # return True

                
        