class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0]
        
        queue = deque()

        adj_list = defaultdict(list)
        degree = {}

        for u,v in edges: 
            adj_list[u].append(v)
            adj_list[v].append(u)
            # degree 
            degree[u] = 1 + degree.get(u, 0)
            degree[v] = 1 + degree.get(v, 0)

        # add nodes with one degree into the queue 
        for i in range(n): 
            if degree[i] == 1: 
                queue.append(i) 
        
        result = []
        while queue: 
            if n <= 2: 
                return list(queue)
            
            for _ in range(len(queue)): 
                node = queue.popleft()
                n -= 1 
        
                for nei in adj_list[node]:
                    degree[nei] -= 1 
                    if degree[nei] == 1: 
                        queue.append(nei) 







        