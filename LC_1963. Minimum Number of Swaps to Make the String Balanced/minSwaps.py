class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        for char in s:
            if char == "[":
                stack.append("[")
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append("]")
        
        return math.ceil((len(stack) // 2) / 2)
