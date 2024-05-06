from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(arr): 
            if len(arr) <=1:
                return arr
            else:
                pivot = arr[0]
                left = [x for x in arr[1:] if x < pivot]
                right = [x for x in arr[1:] if x >= pivot]
                return quickSort(left) + [pivot] + quickSort(right)
        return quickSort(nums)



solution = Solution()
nums = [5,2,3,1]
res = solution.sortArray(nums)
print(res)
