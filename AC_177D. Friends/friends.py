from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solve():
	output = 0
	for node in range (1, V + 1):
		if node not in seen:
			output = max(output, dfs(node))

	return output

def dfs(node):
	output = 1
	seen.add(node)

	for nei in graph[node]:
		if nei not in seen:
			output += dfs(nei)

	return output

# Build graph
graph = defaultdict(list)
V, E = map(int, input().split())
for _ in range (E):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

seen = set()
output = solve()
print(output)
