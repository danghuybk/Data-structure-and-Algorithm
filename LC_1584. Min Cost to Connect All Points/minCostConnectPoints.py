# Prim algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            x, y = points[i], points[j]
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        def cal_weight():
            weight = [[0 for _ in range (N)] for _ in range (N)]
            for i in range (N):
                for j in range (i + 1, N):
                    weight[i][j] = manhattan(i, j)
                    weight[j][i] = weight[i][j]
            return weight
        
        N, output = len(points), 0
        seen, heap, weight =  set(), [(0, 0)], cal_weight()
        
        while len(seen) < N:
            dist, idx = heappop(heap)            
            if idx not in seen:
                output += dist
                seen.add(idx)
                for nei_idx in range(N):
                    if nei_idx not in seen and nei_idx != idx:
                        heappush(heap, (weight[nei_idx][idx], nei_idx))
                
        return output
