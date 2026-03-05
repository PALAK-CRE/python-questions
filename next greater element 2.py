class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        size=len(nums)
        ans=[0]*size

        for ind in range(size-1,-1,-1):
            data=nums[ind]
            while stack and stack[-1] < data:
                    stack.pop()
            if stack:
                 ans[ind]=stack[-1]
            else:
                ans[ind]=-1
            stack.append(data)

        for ind in range(size-1,-1,-1):
            data=nums[ind]
            while stack and stack[-1] < data:
                    stack.pop()
            if stack:
                 ans[ind]=stack[-1]
            else:
                ans[ind]=-1
            stack.append(data)
        return ans