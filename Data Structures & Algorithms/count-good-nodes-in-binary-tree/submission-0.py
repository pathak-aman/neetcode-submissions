# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root,max_seen):
            if root is None:
                return 0
            
            count = 0
            
            if root.val >= max_seen:
                count += 1
                max_seen = root.val
            
            left = traverse(root.left, max_seen)
            right = traverse(root.right, max_seen)

            return count + left + right
        return traverse(root, -float("inf"))
            
            
        #     3
        #   3  
        # 4   2            
        