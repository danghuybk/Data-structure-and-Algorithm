# Similar to Amazon interview question
def solve(N, points):
	maxSum, minSum = -float("inf"), float("inf")
	maxSubstract, minSubstract = -float("inf"), float("inf")

	for x, y in points:
		maxSum = max(maxSum, x + y)
		minSum = min(minSum, x + y)
		maxSubstract = max(maxSubstract, x - y)
		minSubstract = min(minSubstract, x - y)

	return max(maxSum - minSum, maxSubstract - minSubstract)

N = int(input())
points = []
for _ in range (N):
	a, b = map(int, input().split())
	points.append((a, b))

output = solve(N, points)
print(output)
