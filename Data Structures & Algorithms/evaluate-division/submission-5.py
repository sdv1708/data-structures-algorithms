class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        output = []

        graph = defaultdict(list)

        for i in range(len(equations)):
            num, den = equations[i][0], equations[i][1]
            graph[num].append((den, values[i]))
            graph[den].append((num, 1 / values[i]))

        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0

            if src == dest:
                return 1.0

            visited.add(src)
            
            for nei, w in graph[src]:
                if nei not in visited:
                    result = dfs(nei, dest, visited)
                    if result != -1.0:
                        return result * w

            return -1.0

        for query in queries:
            num, den = query[0], query[1]
            output.append(dfs(num, den, set()))

        return output
