# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def height_checker(root):
            if not root:
                return 0
            height_left = height_checker(root.left)
            height_right = height_checker(root.right)
            if abs(height_right - height_left) > 1:
                balanced[0] = False 
                return 0
            return 1 + max(height_left,height_right)    
        height_checker(root)
        return balanced[0]
        

                
        