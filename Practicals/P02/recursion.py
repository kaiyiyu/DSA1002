# Factorial
def calc_factorial(n):
        
    factorial = 1 
        
    if (n == 0): 
            factorial = 1 
    else:
        factorial = n * calc_factorial(n - 1) 

    return factorial

# Fibonacci Sequence
def calc_fibonacci(n):

    fib_value = 0

    if (n == 0):
        fib_value = 0 
    elif (n == 1):
        fib_value = 1 
    else:
        fib_value = calc_fibonacci(n - 1) + calc_fibonacci(n - 2) 

    return fib_value
