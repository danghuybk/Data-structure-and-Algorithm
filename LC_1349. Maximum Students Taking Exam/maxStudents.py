class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        validPos = [0] * rows
        for i in range (rows):
            for j in range (cols):
                validPos[i] |= (1 << j) if seats[i][j] == "." else 0
    
        dp = [[-1 for _ in range (1 << cols)] for _ in range (rows + 1)]
        dp[0][0] = 0
        
        for i in range (1, rows + 1):
            for j in range (0, 1 << cols):
                # Check if state j is a subset of validPos and j hold not left and right adj
                if (j & validPos[i - 1]) != j or (j & (j >> 1)):
                    continue
                for k in range (0, 1 << cols):
                    # Check if state j can be generated from state k or not
                    if not (j & (k >> 1)) and not ((j >> 1) & k) and dp[i - 1][k] != -1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + self.bitCount(j))
        
        return max(dp[rows][col] for col in range (1 << cols))

    def bitCount(self, n: int) -> int:
        bits = 0
        while (n != 0):
            bits += 1
            n &= (n - 1)
        return bits
