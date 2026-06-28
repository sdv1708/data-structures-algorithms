class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 1. Build email -> name map
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                
        # 2. Build adjacency list with emails as nodes, edges between emails in the same account
        # We connect the first email of each account to all other emails in that same account
        graph = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                
        # 3. DFS to find connected components, collecting emails in each component
        visited = set()
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
                    
        # Iterate through all unique emails to find components
        res = []
        for email in email_to_name:
            if email not in visited:
                component = []
                dfs(email, component)
                
                # 4. For each component, look up the name, sort the emails, and format output
                name = email_to_name[email]
                res.append([name] + sorted(component))
                
        return res


        

        

                
            