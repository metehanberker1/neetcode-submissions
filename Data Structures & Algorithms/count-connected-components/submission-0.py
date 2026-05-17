class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i: [] for i in range(n)}

        for u, v in edges:
            preMap[u].append(v)
            preMap[v].append(u)

        destination = set(range(n))
        
        def dfs(i, prev):
            if i not in destination:
                return
            destination.remove(i)
            for nei in preMap[i]:
                if nei == prev:
                    continue
                dfs(nei, i)

        res = 0
        while destination:
            start_node = next(iter(destination))
            dfs(start_node, -1)
            res += 1

        return res