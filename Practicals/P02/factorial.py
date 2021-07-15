# Find the factorial of a number n

def calc_factorial(n):
    if type(n) != int:
        raise TypeError('This function only accepts integers as input.')
    elif n < 0:
        raise ValueError('This function only accepts non-negative integers.')
    
    print('The %d! is equal to %d.' % (n, _calc_factorial(n)))    
        
def _calc_factorial(n):
    
    factorial = 1 
    
    if (n == 0): 
        factorial = 1 
    else:
        factorial = n * _calc_factorial(n - 1) 

    return factorial

calc_factorial(10)

