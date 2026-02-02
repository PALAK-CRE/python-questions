class Solution:
    def moveZeroes(self, nums):
        k = 0  # index for non-zero placement

        # move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # fill remaining positions with zero
        for i in range(k, len(nums)):
            nums[i] = 0