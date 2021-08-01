class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # DFS function
        def dfs(x, y, island_idx, visited):
            output = 1
            grid[x][y] = island_idx
            visited.add((x, y))
            for dirr in dirrs:
                new_x, new_y = x + dirr[0], y + dirr[1]
                if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in visited and grid[new_x][new_y] == 1:
                    output += dfs(new_x, new_y, island_idx, visited)
        
            return output
        
        # Call DFS to remember area os each island
        def record_area(visited, island_area):
            island_idx = 2
            for i in range (N):
                for j in range (N):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        area = dfs(i, j, island_idx, visited)
                        island_area[island_idx] = area
                        island_idx += 1
        
        def main():
            if sum([sum(row) for row in grid]) == N ** 2: return N ** 2
            output = 0
            record_area(visited, island_area)
            for x in range (N):
                for y in range (N):
                    if grid[x][y] != 0: continue
                    connected_area, seen = 1, set()
                    for dirr in dirrs:
                        new_x, new_y = x + dirr[0], y + dirr[1]
                        if 0 <= new_x < N and 0 <= new_y < N:
                            island_idx = grid[new_x][new_y]
                            if island_idx not in seen:
                                connected_area += island_area[island_idx]
                                seen.add(island_idx)
                    output = max(output, connected_area)
            return output
                        
        N, visited, island_area = len(grid), set(), defaultdict(int)
        dirrs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        output = main()
        return output
