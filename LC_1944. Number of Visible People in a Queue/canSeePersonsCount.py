class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        N = len(heights)
        output = [0]
        stack = [heights[-1]]
        
        for i in reversed(range (N - 1)):
            idx = self.binSearch(stack, heights[i])
            if idx == 0:
                output.append(len(stack))
            else:
                output.append(len(stack) - idx + 1)
            while stack and stack[-1] < heights[i]:
                stack.pop()
            stack.append(heights[i])
                
        return output[::-1]

    def binSearch(self, stack, target):
        if not stack or target > stack[0]:
            return 0
        elif target < stack[-1]:
            return len(stack)
        left, right = 0, len(stack) - 1
        while left < right:
            mid = (left + right) // 2
            if stack[mid] > target:
                left = mid + 1
            else:
                right = mid
        return left
