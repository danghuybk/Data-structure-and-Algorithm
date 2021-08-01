from collections import defaultdict, deque

def solve(N, M, K, graph):
	dp = [[0 for _ in range (N)] for _ in range (K + 1)]
	dp[0][0] = 1
	for i in range(1, K + 1):
	    all_sum = sum(dp[i - 1]) % MOD
	    for j in range(N):
	        dp[i][j] = (dp[i][j] + all_sum) % MOD
	        for nei in graph[j]:
	            dp[i][j] = (dp[i][j] - dp[i-1][nei]) % MOD
	
	return dp[K][0]

MOD = 998244353
N, M, K = map(int, input().split())
unstable_road = [[i] for i in range (N)]
for _ in range (M):
	u, v = map(int, input().split())
	unstable_road[u - 1].append(v - 1)
	unstable_road[v - 1].append(u - 1)

output = solve(N, M, K, unstable_road)
print(output)
