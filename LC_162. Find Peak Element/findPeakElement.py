class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = L + (R - L) //2
            if nums[mid] > nums[mid + 1]:
                R = mid
            else:
                L = mid + 1
            
        return L
