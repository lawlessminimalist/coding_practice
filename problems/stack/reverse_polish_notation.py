from typing import List

import operator

# Map string operators to corresponding functions
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda a, b: int(a / b)  # Using floordiv for integer division truncating toward zero
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        loop throught the list in reverse using the operators to distinguish between operands 
        """
        evaluation_stack = []

        if len(tokens) == 1 and tokens[0] not in ops.keys():
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in ops.keys():
                evaluation_stack.append(tokens[i])
            else:
                operand2 = int(evaluation_stack.pop())
                operand1 = int(evaluation_stack.pop())
                output = ops[tokens[i]](operand1,operand2)
                evaluation_stack.append(output)
        return evaluation_stack[0]


print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


                


