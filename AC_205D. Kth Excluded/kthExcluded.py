import bisect
def buildArray(N, nums):
	output = [0]
	for i in range(1, N + 1):
		output.append(nums[i] - nums[i - 1] - 1 + output[i - 1])
	return output

def query(N, K, excludedNumber, nums):
	if K > excludedNumber[-1]:
		return nums[-1] + K - excludedNumber[-1]
	idx = bisect.bisect_left(excludedNumber, K)
	return nums[idx - 1] + K - excludedNumber[idx - 1]

N, Q = map(int, input().split())
nums = [0] + list(map(int, input().split()))
excludedNumber = buildArray(N, nums)
for i in range (Q):
	K = int(input())
	print(query(N, K, excludedNumber, nums))
