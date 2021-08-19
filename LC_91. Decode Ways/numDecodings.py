class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N) + [1]

        for i in range (N - 1, -1, -1):
            if s[i] != '0':
                dp[i] += dp[i + 1]
                if 10 <= int(s[i:i + 2]) <= 26 and i + 2 <= N:
                    dp[i] += dp[i + 2]  
        
        return dp[0]
