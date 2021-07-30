class Solution:
    def tallestBillboard(self, rods):
        # Implement dp by dp: dp[key][value]
        # Key: possible sum
        # Value: Max positive sum
        
        dp = {0:0}

        for rod in rods:
            new_dp = {}
            for key, value in dp.items():
                new_dp[key + rod] = max(new_dp.get(key + rod, 0), value + rod)
                new_dp[key - rod] = max(new_dp.get(key - rod, 0), value)
                new_dp[key] = max(new_dp.get(key, 0), value)
            dp = new_dp
            
        return dp[0]
