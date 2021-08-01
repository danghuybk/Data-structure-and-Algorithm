class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        N, output = len(nums), 0
        MOD = 10 ** 9 + 7
        zero, one, two = 0, 0, 0
        for i in range (0, N):
            if nums[i] == 0:
                zero = ((2 * zero) + 1) % MOD
            elif nums[i] == 1:
                one = (2 * one + zero) % MOD
            else:
                two = (2 * two + one) % MOD           
                output = two
        
        return output 
