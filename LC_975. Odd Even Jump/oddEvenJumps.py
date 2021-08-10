class Solution:
    def oddEvenJumps(self, nums: List[int]) -> int:
        N = len(nums)
        odds, evens = [-1] * N, [-1] * N
        odds = self.smallest_greater_right(N, nums)
        evens = self.greaest_smaller_right(N, nums)
        
        dp = [[0 for _ in range (2)] for _ in range (N)]
        dp[N - 1][0] = dp[N - 1][1] = 1

        for i in range (N - 2, -1, -1):
            dp[i][1] = dp[odds[i]][0] if odds[i] != -1 else 0
            dp[i][0] = dp[evens[i]][1] if evens[i] != -1 else 0
        
        return sum(dp[i][1] for i in range (N))
    
    def smallest_greater_right(self, N, nums):
        output, stack, sorted_list = [-1] * N, [], []
        for i, a in enumerate(nums):
            sorted_list.append((a, i))
        sorted_list.sort()
        for _, i in sorted_list:
            while stack and stack[-1] < i:
                output[stack.pop()] = i
            stack.append(i)
        return output
        
    def greaest_smaller_right(self, N, nums):
        output, stack, sorted_list = [-1] * N, [], []
        for i, a in enumerate(nums):
            sorted_list.append((-a, i))
        sorted_list.sort()
        for _, i in sorted_list:
            while stack and stack[-1] < i:
                output[stack.pop()] = i
            stack.append(i)
        return output
