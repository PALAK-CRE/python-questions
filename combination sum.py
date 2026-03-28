class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, path, target):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Choose
                path.append(candidates[i])
                
                # Stay on same index (reuse allowed)
                backtrack(i, path, target - candidates[i])
                
                # Backtrack
                path.pop()
        
        backtrack(0, [], target)
        return result