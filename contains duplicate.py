class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# Example test cases
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

sol = Solution()

print(sol.containsDuplicate(nums1))  # True
print(sol.containsDuplicate(nums2))  # False
print(sol.containsDuplicate(nums3))  # True