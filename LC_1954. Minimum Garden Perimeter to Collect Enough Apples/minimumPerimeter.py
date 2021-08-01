class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right = 1, 2 * 10 ** 5
        while left < right:
            mid = (left + right) // 2
            if 2 * mid * (mid + 1) * (2 * mid + 1) < neededApples:
                left = mid + 1
            else:
                right = mid
                
        return left * 8
