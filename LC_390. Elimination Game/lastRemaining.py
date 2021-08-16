class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def helper(n, remove_from_left):
            if n == 1:
                return 1
            
            if remove_from_left:
                return 2 * helper(n // 2, False)

            if n % 2 == 1:
                return 2 * helper(n // 2, True)
            
            return 2 * helper(n // 2, True) - 1
    
        return helper(n, True)
