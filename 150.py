class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for value in tokens:
            if value in "+-*/":
                data1 = stack.pop()
                data2 = stack.pop()

                if value == "+":
                    stack.append(data2 + data1)

                elif value == "-":
                    stack.append(data2 - data1)

                elif value == "*":
                    stack.append(data2 * data1)

                elif value == "/":
                    stack.append(int(data2 / data1))

            else:
                stack.append(int(value))

        return stack[-1]