# create class for the recursion algorithms 
class RecursionAlgorithms:

    def __init__(self, n):
        self.n = n

    # Factorial
    def calc_factorial(self):
        
        factorial = 1 
        
        if (self.n == 0): 
            factorial = 1 
        else:
            factorial = self.n * calc_factorial(self.n - 1) 

        return factorial

        print(factorial)

    # Fibonacci Sequence
    def calc_fibonacci(self):

        fib_value = 0

        if (self.n == 0):
            fib_value = 0 
        elif (self.n == 1):
            fib_value = 1 
        else:
            fib_value = calc_fibonacci(self.n - 1) + calc_fibonacci(self.n - 2) 

        return fib_value
