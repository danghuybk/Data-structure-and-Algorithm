def redistribution(N):
	if N <= 2: return 0
	dp = [1] * (N + 1)
	dp[1], dp[2] = 0, 0
	for i in range (3, N + 1):
		dp[i] = (dp[i - 1] + dp[i - 3]) % MOD

	return dp[N]

MOD = 10 ** 9 + 7
N = int(input())
output = redistribution(N)
print(output)
