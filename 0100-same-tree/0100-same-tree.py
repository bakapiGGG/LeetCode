# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkNode(tree_1, tree_2):
            
            if tree_1 is None and tree_2 is None:
                return True
            
            elif tree_1 is None or tree_2 is None:
                return False
            
            elif tree_1.val == tree_2.val:
                return checkNode(tree_1.left, tree_2.left) and checkNode(tree_1.right, tree_2.right)

            
            else:
                return False
            
            
        return checkNode(p, q)
        