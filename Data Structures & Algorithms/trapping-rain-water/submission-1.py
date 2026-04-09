# class Solution:
#     def trap(self, height: List[int]) -> int:

#         l,r = 0, len(height) - 1
#         res = 0
#         current = 0

#         while l < r:
#             cal = (r-l) * min(height[l],height[r])
#             max_area = max(res,cal)
#             print(max_area)
#             if max_area > current:
#                 current  = max_area
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
            
        
#         return current

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res




        