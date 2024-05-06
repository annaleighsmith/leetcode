

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Arrays, two pointers, sorting
    # return like [[0,0,0]] or [] if no possible triplets
    # sum  of 3 integers is 0
    # none of the integers are repeated
    # length of nums is between 3 and 3000
    # -10^5 <= nums[i] <= 10^5

    # [0, 1, 1]
    

    # Know how to get every possible combination of 3 items in a list without rep

    nums.sort()
    n = len(nums)
    result = []

    for i in range(n-2): # how many starting points are there for triplets?
        if i > 0 and nums[i] == nums[i-1]: # if the number is the same as previous skip
            continue
        
        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return result





nums = [0, 1, 1, 5, -1, -1, -5, -5]

res = threeSum(nums)
print(res)
