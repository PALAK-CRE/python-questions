class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, used):
            # Base case
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Choose
                used[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path, used)
                
                # Unchoose (backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result