class Solution:
    def trap(self, height: list[int]) -> int:
        size=len(height)
        leftMax=[0]*size
        rightMax=[0]*size
        
        leftMax[0]=height[0]
        rightMax[size-1]=height[size-1]
        for ind in range(size):
            leftMax[ind]=max(leftMax[ind-1],height[ind])

        for ind in range(size-2,-1,-1):
            rightMax[ind]=max(rightMax[ind+1],height[ind])

        ans=0
        leftMax=height[0]

        for ind in range(size):
            leftMax=max(leftMax,height[ind])
            ans+=min(leftMax,rightMax[ind])-height[ind]
            leftMax=max(leftMax,height[ind])
        return ans