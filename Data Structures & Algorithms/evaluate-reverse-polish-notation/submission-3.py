import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        allowed_operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for i in tokens:
            if i in "+-/*":
                op1 = stack.pop()
                op2 = stack.pop()

                action = allowed_operators[i]
                result = action(op2, op1)

                if i == "/":
                    result = int(result)

                stack.append(result)
            else:
                stack.append(int(i))

        return stack[-1]