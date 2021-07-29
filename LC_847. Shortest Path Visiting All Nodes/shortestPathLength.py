# Floyd + DP on bitmask
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # Shortest path from one node to every node
        # Floyd Marshall algo because N very small
        def floydAlgo():
            dist = [[float("inf") for _ in range (N)] for _ in range (N)]
            for i, adj_list in enumerate(graph):
                dist[i][i] = 0
                for j in adj_list:
                    dist[i][j] = 1
            
            for MID in range (0, N):
                for i in range (0, N):
                    for j in range (0, N):
                        dist[i][j] = min(dist[i][j], dist[i][MID] + dist[MID][j])
            
            return dist
        
        N, output, queue = len(graph), 0, deque()
        dp = [[float("inf") for _ in range (N)] for _ in range (2 ** N)]
        dist = floydAlgo()        
        for i in range (N):
            queue.append((1 << i , i))
            dp[1 << i][i] = 0
            
        while queue:
            curState, curNode = queue.popleft()
            for i in range (N):
                if curState & (1 << i) == 0:
                    if dp[curState][curNode] + dist[curNode][i] < dp[curState | (1 << i)][i]:
                        queue.append((curState | (1 << i), i))
                        dp[curState | (1 << i)][i] = dp[curState][curNode] + dist[curNode][i] 
                        
        return min(dp[2 ** N - 1][i] for i in range (N))
