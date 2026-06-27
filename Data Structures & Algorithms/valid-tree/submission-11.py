class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False 
        
        # build adj list 
        adj_list = defaultdict(list)

        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u) 
        
        visited = set()

        def dfs(node, prev, path):
            if node in visited: 
                return True 
            
            if node in path:
                return False 

            path.add(node) 

            for nei in adj_list[node]: 
                if nei == prev:
                    continue 
                if not dfs(nei, node, path): 
                    return False 
            
            path.remove(node)
            visited.add(node)
            return True 
        
        path = set()
        for i in range(n): 
            if not dfs(i, i, path): 
                return False 
        
        return True 
        
        

