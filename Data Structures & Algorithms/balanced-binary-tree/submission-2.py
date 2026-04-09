# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
same as diameter of a tree -> check for differences by heights

'''
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    
    #dfs
    def Height(self, root):
        
        if root is None:  
            return 0
        
        left, right = self.Height(root.left), self.Height(root.right)
       
        if left < 0 or right < 0 or abs(left - right) > 1:  
            return -1
        
        return 1 + max(left, right)


            
            

        

        