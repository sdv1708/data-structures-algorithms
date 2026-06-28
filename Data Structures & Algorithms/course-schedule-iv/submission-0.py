class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # u -> v, we have to explore the all the neighbors first before we come to u, unlike the previous CS problems 

        reachable = defaultdict(set)

        adj_list = defaultdict(list)
        for prereq, cou in prerequisites: 
            adj_list[prereq].append(cou) # prereq -> cou

        visited = set()

        topolist = []

        def dfs(node): 
            if node in visited:
                return 
            
            for nei in adj_list[node]:
                dfs(nei)
            
            visited.add(node)
            topolist.append(node)
        
        for i in range(numCourses): 
            dfs(i)
        
        for node in topolist: 
            reachable[node].add(node) # a node can reach itself, add it always
            for nei in adj_list[node]: 
                reachable[node] = reachable[node] | reachable[nei]
        
        return [v in reachable[u] for u, v in queries]
        

        

        


