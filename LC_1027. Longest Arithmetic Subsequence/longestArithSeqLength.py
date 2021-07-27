class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        output = 2
        maps = defaultdict(dict)
        
        for i in range (1, N):
            for j in range (0, i):
                diff = A[i] - A[j]
                if diff in maps[j]:
                    maps[i][diff] = maps[j][diff] + 1
                else:
                    maps[i][diff] = 2
                output = max(output, maps[i][diff])
        
        return output
