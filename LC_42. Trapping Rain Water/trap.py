class Solution:
    def trap(self, height: List[int]) -> int:
        N, output = len(height), 0
        left, right = [], []

        for i in range(N):
            if not left or height[i] > left[-1]:
                left.append(height[i])
            else:
                left.append(left[-1])
        
        for i in reversed(range(N)):
            if not right or height[i] > right[-1]:
                right.append(height[i])
            else:
                right.append(right[-1])
        
        for i in range (N):
            output += min(left[i], right[N - i - 1]) - height[i] 
        
        return output
