# Math + DP
class Solution:
    def numDecodings(self, s: str) -> int:
        N, MOD = len(s), 10 ** 9 + 7
        dp = [0] * (N) + [1]
        if s[-1] == '*': dp[-2] = 9
        elif s[-1] != '0': dp[-2] = 1
        
        for i in range (N - 2, -1, -1):
            if s[i] == '0':
                continue
            elif s[i] == '*':
                dp[i] = (dp[i] + 9 * dp[i + 1]) % MOD
                if s[i + 1] == '*':
                    dp[i] = (dp[i] + 15 * dp[i + 2]) % MOD
                elif int(s[i + 1]) <= 6:
                    dp[i] = (dp[i] +  2 * dp[i + 2]) % MOD
                else:
                    dp[i] = (dp[i] + dp[i + 2]) % MOD
            else:
                dp[i] = (dp[i] + dp[i + 1]) % MOD
                if s[i + 1] == '*':
                    if s[i] == '1':
                        dp[i] = (dp[i] + 9 * dp[i + 2]) % MOD
                    elif s[i] == '2':
                        dp[i] = (dp[i] + 6 * dp[i + 2]) % MOD
                else:
                    if 10 <= int(s[i:i + 2]) <= 26:
                        dp[i] = (dp[i] + dp[i + 2]) % MOD
                     
        return dp[0]
