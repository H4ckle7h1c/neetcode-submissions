import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:     
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b) 
        }

        stack = []
        
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue
            
            # operand detected          
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[t](a, b))
        
        return stack[0]
            