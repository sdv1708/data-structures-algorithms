class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        adj_list = defaultdict(list)
        for cou, pre in prerequisites: 
            adj_list[cou].append(pre)

        def dfs(node, path): 

            if node in path: 
                return False

            if node in visited: 
                return True 
            
            path.add(node)

            for nei in adj_list[node]: 
                if not dfs(nei, path): 
                    return False 
            
            path.remove(node)
            visited.add(node)

            return True 

        path = set()
        for cou in range(numCourses): 
            if not dfs(cou, path): 
                return False 
        
        return True 