# Merge sort tree solution
class merge_sort_tree:

	def __init__(self, size, nums):
		self.size = size
		self.nums = nums
		self.tree = [None] * (2 * size)
		self.build_tree()

	def merge_tree(self, nums1, nums2):
		N, M = len(nums1), len(nums2)
		output, p1, p2 = [], 0, 0
		while p1 < N and p2 < M:
			if nums1[p1] < nums2[p2]:
				output.append(nums1[p1])
				p1 += 1
			else:
				output.append(nums2[p2])
				p2 += 1

		output += nums1[p1:] + nums2[p2:]
		return output

	def build_tree(self):
		for i in range (self.size):
			self.tree[i + self.size] = [2 * self.nums[i]]

		for i in range (self.size - 1, 0, - 1):
			self.tree[i] = self.merge_tree(self.tree[2 * i], self.tree[2 * i + 1])

	def query_tree(self, target, start_idx, end_idx):
		output = 0
		start_idx, end_idx = start_idx + self.size, end_idx + self.size

		while start_idx <= end_idx:
			if ((start_idx & 1) > 0):
				output += bisect.bisect_left(self.tree[start_idx], target)
			if ((end_idx & 1) == 0):
				output += bisect.bisect_left(self.tree[end_idx], target)

			start_idx, end_idx = (start_idx + 1) // 2, (end_idx - 1) // 2

		return output

class Solution:
	def reversePairs(self, nums: List[int]) -> int:
		N, output = len(nums), 0
		MST = merge_sort_tree(N, nums)
		for i in range (0, N - 1):
			output += MST.query_tree(nums[i], i + 1, N - 1)
		return output
