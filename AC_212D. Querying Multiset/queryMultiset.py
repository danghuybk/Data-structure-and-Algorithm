from heapq import heappush, heappop

Q, heap, plus = int(input()), [], 0

for i in range (Q):
	query = list(map(int, input().split()))
	if len(query) == 1:
		print(heappop(heap) + plus)
	else:
		if query[0] == 1:
			heappush(heap, query[1] - plus)
		else:
			plus += query[1]
