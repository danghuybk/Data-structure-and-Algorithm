class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def merge(nums1, nums2):
            output = []
            while nums1 or nums2:
                if nums1 > nums2:
                    output += nums1[0],
                    nums1 = nums1[1:]
                else:
                    output += nums2[0],
                    nums2 = nums2[1:]
            return output
                
        def gen_map(nums):
            output = {0: []}
            while len(nums) > k:
                nums = remove_element(nums)
            while len(nums) > 0:
                output[len(nums)] = nums
                nums = remove_element(nums)
            return output
        
        def remove_element(nums):
            min_element, min_index = float("inf"), -1
            for i in range (0, len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return nums[:i] + nums[i + 1:]
            return nums[:len(nums) - 1]
        
        M, N, output = len(nums1), len(nums2), [0] * k
        maps1, maps2 = gen_map(nums1), gen_map(nums2)
        
        for i in range (0, k + 1):
            j = k - i
            if i in maps1 and j in maps2:
                output = max(output, merge(maps1[i], maps2[j]))

        return output
