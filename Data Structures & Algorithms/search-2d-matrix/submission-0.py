class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid_idx = (left + right) // 2
            mid = matrix[mid_idx // cols][mid_idx % cols]

            if mid < target:
                left = mid_idx + 1
            elif mid > target:
                right = mid_idx - 1
            else:
                return True
        return False