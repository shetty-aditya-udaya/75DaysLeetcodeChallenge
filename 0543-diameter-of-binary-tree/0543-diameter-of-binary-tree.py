# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter=0
    def solve(self, node):
        if node is None:
            return 0
        leftheight=self.solve(node.left)
        rightheight=self.solve(node.right)
        self.diameter=max(self.diameter,leftheight+rightheight)
        return 1 + max(leftheight,rightheight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.diameter
        