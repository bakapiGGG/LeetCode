# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        
        def bst_sum(node, low, high):
            
            if node is None:
                return 0
            
            else:
                if node.val < low or node.val > high:
                    return bst_sum(node.left, low, high) + bst_sum(node.right, low, high)
                
                else:
                    return node.val + bst_sum(node.left, low, high) + bst_sum(node.right, low, high)
                
            
        return bst_sum(root, low, high)