def maxSum(arr, k):
    n = len(arr)
    if n<=k:
        return -1
    
    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(n-k): #total length less window size
        print(i)
        window_sum = window_sum - arr[i] + arr[i+k] # sliding window, remove first element and add next
        max_sum = max(window_sum, max_sum) # compare current with previous max

    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))
