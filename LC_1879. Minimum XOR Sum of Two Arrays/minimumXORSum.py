class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        dp = [None for _ in range (2 ** N)]
                
        def dfs(bitmask, i):
            if dp[bitmask] != None:
                return dp[bitmask]
            elif bitmask == 2 ** N - 1:
                dp[bitmask] = 0
                return 0
            
            output = float('inf')
            for j in range(N):
                if (bitmask & (1 << j)) == 0:
                    output = min(output, dfs(bitmask | (1 << j), i + 1) + (nums1[j] ^ nums2[i]))
                
            dp[bitmask] = output
            return output
        
        return dfs(0, 0)
