def calc_factorial(n):
    if type(n) != int:
        raise TypeError('This function only accepts integers as input.')
    elif n < 0: 
        raise ValueError('This function only accepts non-negative integers.')
    print('%d! is equal to %d.' % (n, _calc_factorial(n)))    
    
def _calc_factorial(n):
    factorial = 1
    factorial = 1 if (n == 0) else n * _calc_factorial(n - 1)
    return factorial
calc_factorial(10)
