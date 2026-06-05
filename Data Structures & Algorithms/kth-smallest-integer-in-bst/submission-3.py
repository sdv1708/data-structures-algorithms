# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0 
        result = root.val

        def dfs(node): 
            if not node: 
                return None
            
            nonlocal count, result
         
            value = node.val 
            dfs(node.left)
            count += 1 
            if count == k: 
                result = node.val
            dfs(node.right)
        
        dfs(root)
        return result

        