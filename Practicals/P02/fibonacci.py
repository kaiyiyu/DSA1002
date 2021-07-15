# Find the nth term in the Fibonacci sequence

def calc_fibonacci(n):
    if type(n) != int:
        raise TypeError('This function only accepts integers as input.')
    elif n < 0:
        raise ValueError('This function does not accept negative integers.')
    
    print('The %dth term in the Fibonacci sequence is %d.' % (n, _calc_fibonacci(n)))


def _calc_fibonacci(n):
    
    fib_value = 0

    if (n == 0):
        fib_value = 0
    elif (n == 1):
        fib_value = 1
    else:
        fib_value = _calc_fibonacci(n - 1) + _calc_fibonacci(n - 2) 
    
    return fib_value

calc_fibonacci(17)