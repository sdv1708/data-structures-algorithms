class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list) 

        visited = set()
        
        for u, v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node): # side:
            if node in visited:
                return 
            
            visited.add(node)
            
            for nei in adj_list[node]: 
                dfs(nei)
            
            
        

        count = 0
        for i in range(n): 
            if i not in visited: 
                dfs(i)
                count += 1 
        
        return count