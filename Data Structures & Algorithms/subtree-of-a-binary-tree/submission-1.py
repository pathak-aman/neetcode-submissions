# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None and subRoot:
            return False         
        
        if self.sameTree(root, subRoot):
            return True
        else:
            found_l = self.isSubtree(root.left, subRoot)
            found_r = self.isSubtree(root.right, subRoot)

            return found_l or found_r

    def sameTree(self,root_q, root_p):
            if root_q is None and root_p is None:
                return True
            elif (root_q is None and root_p) or (root_q and root_p is None):
                return False

            if root_q.val == root_p.val:
                same_l = self.sameTree(root_q.left, root_p.left)
                same_r = self.sameTree(root_q.right, root_p.right)

                return same_l and same_r
    
            return False       
            