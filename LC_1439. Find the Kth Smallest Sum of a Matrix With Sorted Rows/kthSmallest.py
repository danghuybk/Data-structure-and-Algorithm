class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        rows, cols = len(mat), len(mat[0])
        heap, visited, curSum, curPath = [], set(), 0, ""
        
        # First path
        for i in range(rows):
            curSum += mat[i][0]
            curPath += "0"
        visited.add(curPath)
        heappush(heap, (curSum, curPath))
        
        # Generator
        while heap:
            curSum, curPath = heappop(heap)
            if k == 1: 
                break
            else: 
                k -= 1
            for i in range (rows):
                if int(curPath[i]) < cols - 1:
                    newPath = int(curPath[i]) + 1
                    newPath = curPath[:i] + str(newPath) + curPath[i + 1:]
                    if newPath not in visited:
                        visited.add(newPath)
                        heappush(heap, (curSum - mat[i][int(curPath[i])] + mat[i][int(curPath[i]) + 1], newPath))
        
        return curSum
