# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.
# You must write an algorithim with O(log N) complexity

class Solution:
    def searchInsert(self, nums, target):
        def search(nums, target):
            midpoint = len(nums)//2
            print(midpoint)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                # target needs to be inserted after the midpoint
                return midpoint + 1 + search(nums[midpoint+1:], target)
            else:
                # right half
                return search(nums[:midpoint], target)

        return search(nums, target)
                    

solution = Solution()
nums = [1,3,5,6,7,8,9,10,11,12,13,14,15,15,15,16,17,18,19,20]
target = 15
res = solution.searchInsert(nums, target)
print(res)
