def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    left = 1
    right = 1

    for i in range(n):
        ans[i] *= left
        left *= nums[i]

        ans[n - 1 - i] *= right
        right *= nums[n - 1 - i]
    
    return ans
        