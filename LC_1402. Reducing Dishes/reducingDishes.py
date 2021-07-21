class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        output = 0
        satisfaction.sort(reverse = True)
        prefixSum = curSum = satisfaction[0]
        for i in range (1, len(satisfaction)):
            prefixSum += satisfaction[i]
            curSum += prefixSum
            output = max(output, curSum)
        return output
