class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. Initialize graph with EVERY unique character
        adj = {char: set() for word in words for char in word}
        
        # 2. Build the graph relationships
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Catch Edge Case: ["abcd", "abc"] -> Invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
                
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # w1[j] comes BEFORE w2[j]
                    break
        
        # 3. Topological Sort via DFS
        visited = {} # False = visiting (current path), True = fully processed
        res = []
        
        def dfs(char):
            if char in visited:
                return visited[char] # Returns True if safe, False if cycle detected
                
            visited[char] = False # Mark as visiting on current path
            
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False # Cycle found deep in recursion
                    
            visited[char] = True # Mark as fully processed
            res.append(char)     # Append post-order
            return True

        # 4. Run DFS on all characters
        for char in adj:
            if not dfs(char):
                return "" # Return empty string if a cycle exists
                
        # Post-order results must be reversed to get correct topological order
        res.reverse()
        return "".join(res)