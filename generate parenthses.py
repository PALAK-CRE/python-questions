class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def isValid(ans):
            stack = []
            for val in ans:
                if val == '(':
                    stack.append(val)
                else:
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
                

        def helperFunction(length, temp):
            if n * 2 == length:
                if isValid(temp):
                    result.append(temp)
                return
            if length > n * 2:
                return

            helperFunction(length + 1, temp + '(')
            helperFunction(length + 1, temp + ')')
            
        helperFunction(0, "")
        return result