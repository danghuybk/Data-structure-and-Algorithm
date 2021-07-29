class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        output, heap = [], []
        buildings.append((2**31, 2**31 + 1, 0))
        
        for L, R, H in buildings:
            # Remove expire elements
            while heap and heap[0][1] <= L:
                remove_H, remove_R = heappop(heap)
                while heap and heap[0][1] <= remove_R:
                    heappop(heap)
                if not heap:
                    output.append((remove_R, 0))
                else:
                    output.append((remove_R, -heap[0][0]))
            
            # Main processing
            if not heap or (heap and H > -heap[0][0]):
                output.append((L, H))
            heappush(heap, (-H, R))
            
        return self.finalResult(output[:-1]) 
    
    def finalResult(self, output):
        stack = []
        for i in range (len(output)):
            while stack and stack[-1][0] == output[i][0]:
                stack.pop()
            if stack and stack[-1][1] == output[i][1]:
                continue
            else:
                stack.append(output[i])
        return stack
