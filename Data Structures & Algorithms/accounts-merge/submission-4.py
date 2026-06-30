class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Build email -> name map
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name

        # build the graph: nodes are the emails  
        graph = defaultdict(list)
        for account in accounts: 
            first_email = account[1]
            for email in account[2:]: 
                graph[first_email].append(email)
                graph[email].append(first_email)
        
        # DFS: collected emails and their connected emails
        visited = set()
        def dfs(node, connected):
            if node in visited:
                return 

            visited.add(node)
            connected.append(node)
            for nei in graph[node]: 
                dfs(nei, connected)

        result = []
        for email in email_to_name: 
            if email not in visited:
                connected = [] 
                dfs(email, connected)

                name = email_to_name[email]
                result.append([name] + sorted(connected))

        return result
                
    

        

        

                
            