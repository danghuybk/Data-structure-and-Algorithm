class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        # Caculate cost to make all substring become palindrome, O(N3)
        def gen_cost_array(N, s):
            cost = [[0 for _ in range (N)] for _ in range (N)]
            for i in range (N):
                for j in range (i + 1, N):
                    cost[i][j] = gen_cost(s[i: j + 1])
            return cost 
    
        def gen_cost(s):
            N, output = len(s), 0
            for i in range (N // 2):
                if s[i] != s[N - i - 1]:
                    output += 1
            return output
            
        # DP
        # dp[k][i] = dp[k - 1][j] + cost[j + 1][i]
        N = len(s)
        cost = gen_cost_array(N, s)
        dp = [[float("inf") for _ in range (N)] for _ in range (K)]
        
        for i in range (N):
            dp[0][i] = cost[0][i]
        
        for k in range (1, K):
            for i in range (N):
                for j in range (0, i):
                    dp[k][i] = min(dp[k][i], dp[k - 1][j] + cost[j + 1][i])        
        
        return dp[K - 1][N - 1]
