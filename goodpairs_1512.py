
# Problem: Good Pairs
# Given an array of integers nums, return the good pairs
# A pair (i, j) is called good if nums[i] == nums[j] and i < j
# You cant double count pairs in the array
# i < j is always true anyway?

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force solution
        # output = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] == nums[j]):
        #             output += 1
        # return output

        # optimized solution
        hashy = {} # key is the number and the value will be number of time traversed
        output = 0
        for n in nums:
            print("n: ", n)
            print(hashy)
            if n in hashy: # if the number is already a key in dict...
                output += hashy[n]
                hashy[n] += 1
            else:
                hashy[n] = 1
        return output

        


solution = Solution()
nums = [1, 2, 3, 1, 1, 3]
print(f"nums: {nums}")
result = solution.numIdenticalPairs(nums)
print(result)
