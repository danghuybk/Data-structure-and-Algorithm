class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[0 for _ in range (2)] for _ in range (N)]
        output = dp[0][0] = arr[0]
        for i in range (1, N):
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i - 1][1] + arr[i], arr[i], dp[i - 1][0])
            output = max(output, dp[i][0], dp[i][1])
        
        return output
