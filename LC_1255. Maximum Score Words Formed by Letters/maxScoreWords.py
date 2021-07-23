# Generate all possible valid set base on bit manipulation and counter, then check max score

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        N, output, lettersCounter = len(words), 0, Counter(letters)
        for i in range (1, 2 ** N):
            binArray = self.decToBin(N, i)
            wordsCounter = Counter()
            for i, num in enumerate(binArray):
                if num == 1: 
                    wordsCounter += Counter(words[i])
                    
            if self.isValidSet(wordsCounter, lettersCounter):
                curScore = 0
                for key, value in wordsCounter.items():
                    curScore += value * score[ord(key) - ord("a")]
                output = max(output, curScore)
                
        return output
    
    def decToBin(self, N, num):
        stack = []
        while num:
            stack.append(num % 2)
            num //= 2
        if len(stack) < N:
            return stack + [0] * (N - len(stack))
        else:
            return stack
    
    def isValidSet(self, wordsCounter, lettersCounter):
        for key in wordsCounter.keys():
            if wordsCounter[key] > lettersCounter[key]:
                return False
        return True
