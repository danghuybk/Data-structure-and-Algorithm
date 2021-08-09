from collections import defaultdict
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(parent, node):
	if len(visited) == N and node == 1:
		return None

	output.append(str(node))
	visited.add(node)
	
	while graph[node]:
		nei = heappop(graph[node])
		if nei not in visited:
			dfs(node, nei)

	if parent > 0:
		output.append(str(parent))

N = int(input())
output, visited, graph = [], set(), defaultdict(list)
for _ in range(N - 1):
	u, v = map(int, input().split())
	heappush(graph[u], v)
	heappush(graph[v], u)

dfs(-1, 1)
print(" ".join(output))
