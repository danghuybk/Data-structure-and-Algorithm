# Using 01-BFS, for 2 operation, using appendleft got TLE
# Optimize by using append to reduce not necessary computation

from collections import deque

def solve():
	queue = deque([(sx, sy)])
	while queue:
		x, y = queue.popleft()

		for dirr in dirrs:
			new_x, new_y = x + dirr[0], y + dirr[1]
			if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "." and dist[new_x][new_y] > dist[x][y]:
				dist[new_x][new_y] = dist[x][y]
				queue.appendleft((new_x, new_y))

		for i in range (-2, 3):
			for j in range (-2, 3):
				new_x, new_y = x + i, y + j
				if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == "." and dist[new_x][new_y] > dist[x][y] + 1:
					dist[new_x][new_y] = dist[x][y] + 1
					queue.append((new_x, new_y))

	return dist[ex][ey] if dist[ex][ey] != float("inf") else -1


dirrs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rows, cols = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1

dist = [[float("inf") for _ in range (cols)] for _ in range (rows)]
dist[sx][sy] = 0

grid = []
for i in range (rows):
	row = list(input())
	grid.append(row)

output = solve()
print(output)
