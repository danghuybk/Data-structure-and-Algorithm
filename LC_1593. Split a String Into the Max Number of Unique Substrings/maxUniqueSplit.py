class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Backtracking
        def helper(startIdx, path):
            nonlocal output
            for i in range (startIdx, N):
                candidate = s[startIdx:i + 1]
                if candidate not in path:
                    path.append(candidate)
                    
                    if i == N - 1:
                        output = max(output, len(path))
                    else:
                        helper(i + 1, path)
                    
                    path.pop()
                
        # Main processing
        N, output, seen = len(s), 0, set()
        helper(0, [])
        return output 
