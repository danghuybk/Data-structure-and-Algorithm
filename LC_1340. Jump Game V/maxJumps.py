class Solution:
    def maxJumps(self, nums: List[int], d: int) -> int:
        N, dp, heap = len(nums), [1] * len(nums), []
        
        for idx, num in enumerate(nums):
            heappush(heap, (num, idx))
            
        while heap:
            num, i = heappop(heap)
            cur_max = 0
            for delta in range (1, d + 1):
                j = i + delta
                if j >= N: break
                cur_max = max(cur_max, nums[j])
                if nums[i] > cur_max:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            
            cur_max = 0
            for delta in range (1, d + 1):
                j = i - delta
                if j < 0: break
                cur_max = max(cur_max, nums[j])
                if nums[i] > cur_max:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break

        return max(dp)
