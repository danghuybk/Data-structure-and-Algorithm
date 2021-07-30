class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N, MOD = len(board), 10 ** 9 + 7
        dp = [[[-1, 0] for _ in range (N + 1)] for _ in range (N + 1)]
        dp[0][0] = [0, 1]
        
        for i in range (1, N + 1):
            for j in range (1, N + 1):
                if board[i - 1][j - 1] == "X":
                    dp[i][j] = [-1, 0]
                else:
                    maxNeiScore = - float("inf")
                    neis = [[i - 1, j - 1], [i, j - 1], [i - 1, j]]
                    for r, c in neis:
                        maxNeiScore = max(maxNeiScore, dp[r][c][0])
                        
                    if maxNeiScore == -1:
                        dp[i][j] = [-1, 0]
                    else:
                        maxNeiScoreFreq = 0
                        for r, c in neis:
                            if dp[r][c][0] == maxNeiScore:
                                maxNeiScoreFreq = (maxNeiScoreFreq + dp[r][c][1]) % MOD
                        number = 0 if board[i - 1][j - 1] in ["S", "E"] else int(board[i - 1][j - 1])
                            
                        dp[i][j] = [maxNeiScore + number, maxNeiScoreFreq]
        
        return dp[N][N] if dp[N][N][0] != -1 else [0, 0]
