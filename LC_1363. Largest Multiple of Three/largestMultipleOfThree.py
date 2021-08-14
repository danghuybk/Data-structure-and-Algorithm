class Solution:
    def largestMultipleOfThree(self, nums: List[int]) -> str:
        # Same with https://leetcode.com/problems/greatest-sum-divisible-by-three/
        # Initialize
        N, SUM, MOD, INF = len(nums), sum(nums), sum(nums) % 3, float("inf")
        
        # Base case
        if MOD == 0:
            nums.sort(reverse = True)
            return "".join(str(num) for num in nums) if nums[0] else "0"
        
        # General case, find smallest sum equal to MOD and save the index
        min_sum_mod_1, min_sum_mod_2 = [INF, INF, []], [INF, INF, []]
        for i in range (N):
            if nums[i] % 3 == 1:
                min_sum_mod_2 = min(min_sum_mod_2, [min_sum_mod_1[0] + 1, min_sum_mod_1[1] + nums[i], min_sum_mod_1[2] + [i]])
                min_sum_mod_1 = min(min_sum_mod_1, [1, nums[i], [i]])
            elif nums[i] % 3 == 2:
                min_sum_mod_1 = min(min_sum_mod_1, [min_sum_mod_2[0] + 1,min_sum_mod_2[1] + nums[i], min_sum_mod_2[2] + [i]])
                min_sum_mod_2 = min(min_sum_mod_2, [1, nums[i], [i]])
        
        remove_idx = min_sum_mod_1[2] if MOD == 1 else min_sum_mod_2[2]
        while remove_idx:
            idx = remove_idx.pop()
            nums = nums[:idx] + nums[idx + 1:]

        nums.sort(reverse = True)
        if not nums:
            return ""
        elif nums[0] == 0:
            return "0"
        return "".join(str(num) for num in nums)
