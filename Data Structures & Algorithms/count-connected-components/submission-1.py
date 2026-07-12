class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i: [] for i in range(n)}

        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        destination = set(range(n))
        visited = set()
        
        def dfs(i):
            if i not in destination:
                return
            destination.remove(i)
            visited.add(i)
            for nei in preMap[i]:
                if nei in visited:
                    continue
                dfs(nei)

        res = 0
        while destination:
            start_node = next(iter(destination))
            dfs(start_node)
            res += 1

        return res