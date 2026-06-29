class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)): 
            num, den = equations[i][0], equations[i][1]
            graph[num].append((den, values[i]))
            graph[den].append((num, 1 / values[i]))
        
        
        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1 
             
            if src == target: 
                return 1 
            
            visited.add(src)

            for nei, w in graph[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1: 
                        return result * w 
            
            return -1 
        
        result = []
        for query in queries: 
            result.append(dfs(query[0], query[1], set()))

        return result 