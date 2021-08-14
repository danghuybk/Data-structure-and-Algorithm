class Solution:
    def minFallingPathSum(self, nums: List[List[int]]) -> int:
        N = len(nums)
        dp = [[0 for _ in range (N)] for _ in range (N)]
        for i in range (N):
            dp[0][i] = nums[0][i]
        
        for i in range (1, N):
            min_previous = self.min_except_self(N, dp[i - 1])
            for j in range (N):
                dp[i][j] = min_previous[j] + nums[i][j]
        
        return min(dp[N - 1])
    
    def min_except_self(self, N, nums):
        output, left, right = [], [float("inf")] * N, [float("inf")] * N    
        for i in range (1, N):
            left[i] = min(left[i - 1], nums[i - 1])
        for i in range (N - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i + 1])
        for i in range (N):
            output.append(min(left[i], right[i]))
        return output
