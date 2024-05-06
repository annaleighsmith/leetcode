from typing import List

# find largest positive integer k that has k*-1 also in array


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hash = {}
        for i, num in enumerate(sorted(nums, reverse=True)):
            if num > 0:
                hash[num] = i
        for num in sorted(nums):
            if num < 0:
                if abs(num) in hash:
                    return abs(num)
        return -1
        # return -1


# nums = [-1, 10, 6, 7, -7, 1]
nums = [-1, 2, -3]
solution = Solution().findMaxK(nums)
print(solution)
