class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for value in s:
            # push opening brackets onto stack
            if value in "([{":
                stack.append(value)
            else:
                # must have a matching opening bracket
                if not stack:
                    return False
                top = stack[-1]
                if (
                    (top == "(" and value == ")")
                    or (top == "[" and value == "]")
                    or (top == "{" and value == "}")
                ):
                    stack.pop()
                else:
                    return False
        # valid if no unmatched openings remain
        return not stack