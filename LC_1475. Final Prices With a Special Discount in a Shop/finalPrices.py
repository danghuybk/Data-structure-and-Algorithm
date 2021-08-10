class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N, stack = len(prices), []
        output = [None] * N
        for i in range (N - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                output[i] = prices[i] - stack[-1]
            else:
                output[i] = prices[i]
            
            stack.append(prices[i])
        return output
