class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        visited = set()
        
        adj_list = defaultdict(list)

        for cou, pre in prerequisites: 
            adj_list[cou].append(pre)
        
        def dfs(node, path): 
            if node in visited: 
                return True 

            if node in path: 
                return False
            
            path.add(node)

            for pre in adj_list[node]: 
                if not dfs(pre, path): 
                    return False 

            path.remove(node)
            visited.add(node)
            result.append(node)

            return True 
        
        path = set()
        for cou in range(numCourses): 
            if not dfs(cou, path): 
                return []
        
        return result




        


        