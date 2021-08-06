class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if self.is_possible(nums, k, mid):
                left = mid + 1
            else:
                right = mid 
        
        return left
        
    def is_possible(self, nums, k, target):
        count, left = 0, 0
        for right, num in enumerate(nums):
            while left < right and num - nums[left] > target:
                left += 1
                
            count += right - left
        
        return count < k
