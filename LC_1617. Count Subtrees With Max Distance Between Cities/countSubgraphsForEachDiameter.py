class Solution:
    def countSubgraphsForEachDiameter(self, N: int, edges: List[List[int]]) -> List[int]:
        # Distance between any pairs of node
        def floydWarshall(): 
            dist = [[float("inf") for _ in range (N + 1)] for _ in range (N + 1)]
            for u, v in edges:
                dist[u][v] = 1
                dist[v][u] = 1
            
            for MID in range (1, N + 1):
                for i in range (1, N + 1):
                    for j in range (1, N + 1):
                        dist[i][j] = min(dist[i][j], dist[i][MID] + dist[MID][j])
        
            return dist
        
        # A subtree is valid if and only if edges + 1 = number of nodes
        def getTreeMaxDist(N, nodes):
            output, edges = 0, 0
            for i in range (N):
                for j in range (i + 1, N):
                    if dist[nodes[i] + 1][nodes[j] + 1] == 1:
                        edges += 1
                    output = max(output, dist[nodes[i] + 1][nodes[j] + 1])
            return output if edges + 1 == N else 0
        
        output = [0] * (N)
        dist = floydWarshall()
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for bitmask in range (1, 1 << N):
            nodes = []
            for i in range (0, N):
                if bitmask & (1 << i):
                    nodes.append(i)
            output[getTreeMaxDist(len(nodes), nodes)] += 1
        
        return output[1:]
