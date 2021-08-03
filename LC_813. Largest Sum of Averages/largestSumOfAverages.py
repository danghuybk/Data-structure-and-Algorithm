# Time: O(K * N ^ 2)
# Space: O(K * N)
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        
        def average(i, j):
            return (prefix_sum[j] - prefix_sum[i]) / (j - i) 
        
        N = len(A)
        
        # Caculate prefix sum
        prefix_sum = [0]
        for i in range (N): 
            prefix_sum.append(prefix_sum[-1] + A[i])
        
        # Base case
        dp = [[0 for i in range (N)] for _ in range (K)]
        for i in range (N):
            dp[0][i] = average(i, N)
            
        # Main processing        
        for k in range(1, K):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[k][i] = max(dp[k][i], average(i, j) + dp[k - 1][j])

        return dp[K - 1][0]
