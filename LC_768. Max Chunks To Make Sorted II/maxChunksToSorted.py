class Solution:
    def maxChunksToSorted(self, nums: List[int]) -> int:
        N, output = len(nums), 1
        if N == 1: return output
        
        smallest_after, biggest_left = [0] * (N - 1), [nums[0]]
        
        cur_max = nums[0]
        for i in range (1, N):
            cur_max = max(cur_max, nums[i])
            biggest_left.append(cur_max)
        
        smallest_after[-1] = nums[-1]
        cur_min = nums[-1]
        for i in range (N - 3, -1, -1):
            cur_min = min(cur_min, nums[i + 1])
            smallest_after[i] = cur_min

        for i in range (0, N - 1):
            if biggest_left[i] <= smallest_after[i]:
                output += 1
        
        return output
