# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, node):
        if node is None:
            return (True, 0)

        left_balanced, left_height = self.checkHeight(node.left)
        right_balanced, right_height = self.checkHeight(node.right)

        if left_balanced == False or right_balanced == False:
            return (False, 0)
        
        if abs(left_height - right_height) > 1:
            return (False, 0)
        
        current_height = max(left_height, right_height) + 1
        return (True, current_height)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.checkHeight(root)
        return balanced