# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """ For the node you want to delete 
            1) No children: return None 
            2) One Child: return the child which exists 
            3) Two ChildrenL in-order successor (left most node in the right subtree),
               replace the current nodes value and then delete that successor from the right subtree"""
        
        def getMin(node): 
            while node.left:
                node = node.left
            return node 
        if not root:
            return None 
        
        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        # case where you find the node you want to delete 
        else: 
            if not root.right: 
                return root.left
            elif not root.left: 
                return root.right
            else: 
                successor = getMin(root.right)
                root.val = successor.val 
                # deleting the duplicate child node which was just promoted 
                root.right = self.deleteNode(root.right, successor.val) 
            
        return root

        