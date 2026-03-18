class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for value in s:
    
            if value == "(" or value == "[" or value == "{":
                stack.append(value)

            
            elif len(stack) == 0:
                return False

            # Matching pairs
            elif (
                (stack[-1] == "(" and value == ")") or
                (stack[-1] == "[" and value == "]") or
                (stack[-1] == "{" and value == "}")
            ):
                stack.pop()

            else:
                return False

        
        if len(stack) == 0:
            return True
        else:
            return False