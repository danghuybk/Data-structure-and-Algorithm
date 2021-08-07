from heapq import heappush, heappop
def two_buttons(N, M):
	if N >= M:
		return N - M
	output, queue, min_dist = 0, [(0, N)], {}

	while queue:
		cur_dist, cur_number = heappop(queue)
		
		if cur_number not in min_dist:
			min_dist[cur_number] = cur_dist
			if cur_number >= 1 and cur_number - 1 not in min_dist:
				heappush(queue, (cur_dist + 1, cur_number - 1))
			if cur_number <= M and cur_number * 2 not in min_dist:
				heappush(queue, (cur_dist + 1, cur_number * 2))

	return min_dist[M]

N, M = map(int, input().split())
output = solve(N, M)
print(output)
