class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def is_possible(target):
            visited, queue, blocks = set(), deque(), set()
            for x, y in cells[:target]:
                blocks.add((x - 1, y - 1))
            for j in range (col):
                if (0, j) not in blocks:
                    queue.append((0, j))
                    visited.add((0, j))
                    
            while queue:
                cur_x, cur_y = queue.popleft()
                if cur_x == row - 1:
                    return True
                for dirr in dirrs:
                    new_x, new_y = cur_x + dirr[0], cur_y + dirr[1]
                    if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in blocks and (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            
            return False
                    
            
        dirrs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        left, right = 1, row * col
        while left < right:
            mid = (left + right + 1) // 2
            if is_possible(mid):
                left = mid
            else:
                right = mid - 1
        return left
