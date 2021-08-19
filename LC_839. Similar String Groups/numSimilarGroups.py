class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:     
        
        def dfs(start_idx):
            visited.add(start_idx)
            for j in range (0, N):
                if j not in visited and similar(strs[start_idx], strs[j]):
                    dfs(j)
        
        N, M, output, visited = len(strs), len(strs[0]), 0, set()
        similar = lambda x, y: sum(a != b for a, b in zip(x, y)) <= 2
        for idx in range (N):
            if idx not in visited:
                dfs(idx)
                output += 1
        
        return output
