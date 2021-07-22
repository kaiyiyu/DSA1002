import DSAQueue
import DSAStack

class EquationSolver:
    
    def __init__(self):
        pass
    
    def solve_equation(self, equation):
        postfix_queue = self._parse_infix_postfix(equation)
        return self._evaluate_postfix(postfix_queue)
    
    def _parse_infix_postfix(self, equation):
        infix_array = str(equation).split(' ')
        op_stack = DSAStack.DSAStack()
        postfix_queue = DSAQueue.DSAQueue()
        OPERATORS = '+-*/'
        
        for term in infix_array:
            if term == '(':
                op_stack.push(term)
            elif term == ')':
                while op_stack.top() != '(':
                    postfix_queue.enqueue(op_stack.pop())
                op_stack.pop()
            elif term in OPERATORS:
                while not op_stack.is_empty() and op_stack.top() != '(' and self._precedence_of(op_stack.top()) >= self._precedence_of(term):
                    postfix_queue.enqueue(op_stack.pop())
                op_stack.push(term)
            else:
                postfix_queue.enqueue(float(term))
                
        while not op_stack.is_empty():
            postfix_queue.enqueue(op_stack.pop())
        
        postfix_queue.display()
        return postfix_queue
    
    def _evaluate_postfix(self, postfix_queue):
        operand_stack = DSAStack.DSAStack()
        while not postfix_queue.is_empty():
            if isinstance(postfix_queue.peek(), (float, int)):
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
            raise Exception("Invalid operation.")
        
if __name__ == "__main__":
    exp1 = EquationSolver()
    answer1 = exp1.solve_equation('3 * 4')
    print(answer1)
    
    exp2 = EquationSolver()
    answer2 = exp2.solve_equation("2 - 4 + 3")
    print(answer2)
    
    exp3 = EquationSolver()
    answer3 = exp3.solve_equation("( 4 + 2 ) * 3")
    print(answer3)
    
    exp4 = EquationSolver()
    answer4 = exp4.solve_equation("( ( 2 - 3 ) / 4 * ( 1 + 9 ) ) * 2")
    print(answer4)
    
    exp5 = EquationSolver()
    answer5 = exp5.solve_equation("( 10.3 * ( 14 + 3.2 ) ) / ( 5 + 2 - 4 * 3 )")
    print(answer5)
