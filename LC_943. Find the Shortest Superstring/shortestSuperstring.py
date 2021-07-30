class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        N, MAX = len(words), float("inf")
        state = 1 << N
        dp = [[[MAX, ""] for _ in range (N)] for _ in range (state)]
        for i in range (N):
            dp[1 << i][i] = [len(words[i]), words[i]]
        
        for bitmask in range (1, state):
            for i in range (N):
                # Consider i as the last bit
                if bitmask & (1 << i) == 0:
                    continue
                
                # Consider all previous state that can create i
                smallestCand = [MAX, ""]
                for j in range (N):
                    if j != i and bitmask & (1 << j):
                        cand = self.mergeWords(dp[bitmask ^ (1 << i)][j][1], words[i])
                        smallestCand = min(smallestCand, [len(cand), cand])
                
                if smallestCand[0] != MAX:
                    dp[bitmask][i] = smallestCand

        return min(dp[state - 1])[1]
        
    def mergeWords(self, word1, word2):
        if not word1: return word2
        N, M = len(word1), len(word2)
        for i in range(M, 0, -1):
            if N - i >= 0 and word1[-i:] == word2[:i]:
                return word1 + word2[i:]
        
        return word1 + word2
