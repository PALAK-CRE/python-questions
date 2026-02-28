class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        path = path.split('/')
        
        for value in path:
            if value == "" or value == ".":
                continue
            
            elif value == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(value)
        
        return "/" + "/".join(stack)