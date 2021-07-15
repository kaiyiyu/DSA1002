# Convert decimal x (base 10) to base y

def convert_decimal(x, y):
    if type(x) != int or type(y) != int:
        raise TypeError('This function only works with integer inputs.')
    elif x < 0 or y < 0: 
        raise ValueError('This function does not accept negative input.')
    elif y == 0:
        raise ZeroDivisionError('Can not divide by 0.')
    elif y > 16:
        raise ValueError('This function only converts up to base 16.')
    
    print('In the base %d number system, decimal %d is considered as %s.' % (y, x, _convert_decimal(x, y)))

def _convert_decimal(x, y):
    
    rem = x % y

    if x <= 1:
        return str(x)
    else:
        return str(_convert_decimal(x//y, y)) + str(rem)
    
convert_decimal(56789, 2)