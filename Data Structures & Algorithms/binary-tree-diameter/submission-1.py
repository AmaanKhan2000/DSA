# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def height(root):
            if not root:
                return 0
            height_left = height(root.left)
            height_right = height(root.right)
            sub_dia = height_left + height_right
            diameter[0] = max(sub_dia,diameter[0])
            return 1 + max(height_left, height_right)
        height(root)
        return diameter[0]    

        