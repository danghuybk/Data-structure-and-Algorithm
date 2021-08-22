# Sliding window
# O(N) time, O(1) space
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, M, output = len(s), len(p), []
        cand, target = Counter(), Counter(p)
        for i in range (0, N):
            cand[s[i]] += 1
            if i >= M:
                if cand[s[i - M]] == 1:
                    del cand[s[i - M]]
                else:
                    cand[s[i - M]] -= 1
            
            if cand == target:
                output.append(i - (M - 1))
                
        return output
