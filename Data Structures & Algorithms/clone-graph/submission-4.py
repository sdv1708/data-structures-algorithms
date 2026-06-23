"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}

        def dfs(node): 
            if node in mapping: 
                return mapping[node] 
            
            clone = Node(node.val)
            mapping[node] = clone 

            for nei in node.neighbors:
                all_nei = dfs(nei)
                clone.neighbors.append(all_nei)
            
            return clone
        
        return dfs(node) if node else None
        