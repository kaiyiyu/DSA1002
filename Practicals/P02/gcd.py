# Find the GCD of two numbers using the Euclidean Algorithm (assumes a and b are non-negative)

def calc_gcd(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError('This function only works with integer inputs.')
    elif a < 0 or b < 0:
        raise ValueError('This function only works with positive integers.')
    
    print('The GCD of %d and %d is %d.' % (a, b, _calc_gcd(a, b)))

def _calc_gcd(a, b):
    
    if b == 0:
        return a
    else:
        return _calc_gcd(b, a % b)

calc_gcd(69, 1024)



