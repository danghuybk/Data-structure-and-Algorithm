class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])
        top, bottom = 0, M - 1
        while top < bottom:
            mid = (top + bottom) // 2
            
            if mid == N - 1 or max(mat[mid]) > max(mat[mid + 1]):
                bottom = mid
            else:
                top = mid + 1
        
        row, col = bottom, 0
        for i in range (1, N):
            if mat[row][i] > mat[row][col]:
                col = i
        return [row, col]
