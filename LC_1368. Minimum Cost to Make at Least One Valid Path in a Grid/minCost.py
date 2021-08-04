class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        min_dist, heap = {}, [(0, 0, 0)]
        dirrs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while heap:
            cur_cost, cur_x, cur_y = heappop(heap)
            if cur_x == rows - 1 and cur_y == cols - 1:
                return cur_cost
            if (cur_x, cur_y) in min_dist:
                continue
            min_dist[(cur_x, cur_y)] = cur_cost
            
            for i, dirr in enumerate(dirrs):
                new_x, new_y = cur_x + dirr[0], cur_y + dirr[1]
                if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in min_dist: 
                    if i + 1 == grid[cur_x][cur_y]:
                        heappush(heap, (cur_cost, new_x, new_y))
                    else:
                        heappush(heap, (cur_cost + 1, new_x, new_y))
                            
