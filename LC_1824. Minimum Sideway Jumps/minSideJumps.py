class Solution:
    def minSideJumps(self, arr: List[int]) -> int:
        N, dp = len(arr), [0] * 4
        dp[1] = dp[3] = 1
        
        for i in range (1, N):
            dp[arr[i]] = float("inf")
            min_jump = min(dp[1:4])
            for j in range (1, 4):
                if j != arr[i]:
                    dp[j] = min(dp[j], min_jump + 1)
            
        return min(dp[1:4])
