import DSAQueue
import DSAStack
class EquationSolver:
    
    def __init__(self):
        pass
    
    def solve_equation(self, equation):
        postfix_queue = self._parse_infix_postfix(equation)
        return self._evaluate_postfix(postfix_queue)
    
    def infix_to_postfix(self, equation): 
        stack = []
        postfix = ''

        for term in equation:
            if term not in OPERATORS:  # if an operand then put it directly in postfix expression

                output+= term

            elif term =='(':  # else operators should be put in stack

                stack.append('(')

            elif term ==')':
                while stack and stack[-1]!= '(':
                    output+=stack.pop()
                stack.pop()
            else:
                while stack and stack[-1]!='(' and PRIORITY[term ]<=PRIORITY[stack[-1]]:
                    output+=stack.pop()
                stack.append(term )
    while stack:
        output+=stack.pop()
    return output
    
    def _evaluate_postfix(self, postfix_queue):
        operand_stack = DSAStack.DSAStack()
        while not postfix_queue.is_empty():
            if isinstance(postfix_queue, float):
                operand_stack.push(postfix_queue.dequeue())
            else:
                op2 = float(operand_stack.pop())
                op1 = float(operand_stack.pop())
                op = postfix_queue.dequeue()
                operand_stack.push(self._execute_operation(op, op1, op2))
        
        return float(operand_stack.pop())
       
    def _precedence_of(self, the_operator):  # sourcery skip: merge-comparisons
        if the_operator == '+' or the_operator == '-':
            precedence = 1
        elif the_operator == '*' or the_operator == '/':
            precedence = 2
        return precedence
        
    def _execute_operation(self, op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        elif op == "-":
            return op1 - op2
        else:
            raise Exception("Invalid operator.")
        
if __name__ == "__main__":
    exp = EquationSolver()
    
    exp.solve_equation((3 * 8) - 12 / 4)
    