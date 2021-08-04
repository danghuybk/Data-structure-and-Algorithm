class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        output, queue, seen = [], deque([(0, s)]), set()
        while queue:
            size = len(queue)
            for _ in range (size):
                min_remove, cur_s = queue.popleft()
                if self.isValid(cur_s):
                    output.append(cur_s)
                for i in range (len(cur_s)):
                    cand = cur_s[:i] + cur_s[i + 1:]
                    if cand not in seen:
                        queue.append((min_remove + 1, cand))
                        seen.add(cand)
                        
            if output:
                return output
        
        return [""]
    
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
