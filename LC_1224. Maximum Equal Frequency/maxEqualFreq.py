# There are four cases:
# 1. All element occurs only 1
# 2. Every element is the same
# 3. 4. There are two occurence: N - 1 same and the other occur 1 or occur more than other only 1
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        N, output = len(nums), 0
        freq, freqCount = defaultdict(int), defaultdict(int)
        for i in range (0, N):
            if freq[nums[i]] in freqCount:
                if freqCount[freq[nums[i]]] == 1:
                    del freqCount[freq[nums[i]]]
                else:
                    freqCount[freq[nums[i]]] -= 1
                    
            freq[nums[i]] += 1
            freqCount[freq[nums[i]]] += 1  
            
            if self.isValid(freqCount):
                output = i + 1

        return output
    
    def isValid(self, freqCount):
        if len(freqCount) > 2:
            return False
        elif len(freqCount) == 1:
            if list(freqCount.keys())[0] == 1 or list(freqCount.values())[0] == 1:
                return True
            else:
                return False
        
        minFreq = min(freqCount.keys())
        maxFreq = max(freqCount.keys())
        if minFreq + 1 == maxFreq and freqCount[maxFreq] == 1:
            return True
        if minFreq == 1 and freqCount[minFreq] == 1:
            return True
        
        return False
