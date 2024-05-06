
# array, hash table

# one pass
def twoSum(nums, target):
    hashy = {} # create a hash table of all the nums
    for i, num in enumerate(nums):
        search = target-num
        if search in hashy:
            return[hashy[search], i]
        hashy[num] = i
    return []

# two pass
def twoSumTwo(nums, target):
    hashy = {}
    for i, num in enumerate(nums):
        hashy[num] = i
    for i, num in enumerate(nums):
        search = target-num
        if search in hashy and hashy[search] != i:
            return[i, hashy[search]]



nums = [2, 7, 11, 15]
target = 9
print(f"nums: {nums}")
print(f"target: {target}")
res = twoSum(nums, target)
print(res)
