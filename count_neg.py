from typing import List

# already sorted in decreasing order row and columns wise
# return number of neagitve numbers in the grid

class Solution:
    def countNegatives(self, grid: List[List[int]]):
        def binary_search(nums):
            left, right = 0, len(nums)
            while left < right:
                midpoint = left + (right - left) // 2
                print(midpoint)
                if nums[midpoint] < 0:
                    right = midpoint
                else:
                    left = midpoint + 1 # shift midpoint to right
            return len(nums) - left
        return sum(binary_search(g) for g in grid)


solution = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
res = solution.countNegatives(grid)

print(res)
