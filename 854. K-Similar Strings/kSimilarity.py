class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        N, queue, output = len(s1), [(0, 0, s1)], float("inf")
        minDist = {}
        
        while queue:
            curDist, curIdx, curWord = heappop(queue)
            if curWord == s2:
                return curDist

            minDist[curWord] = curDist

            if curWord[curIdx] == s2[curIdx]:
                heappush(queue, (curDist, curIdx + 1, curWord))
            else:
                for j in range (curIdx + 1, N):
                    if curWord[j] == s2[curIdx]:
                        cand = self.getCand(curWord, curIdx, j)
                        if cand not in minDist:
                            heappush(queue, (curDist + 1, curIdx + 1, cand))
    
    def getCand(self, word, i, j):
        cand = list(word)
        cand[i], cand[j] = cand[j], cand[i]
        return "".join(cand)
