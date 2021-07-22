import DSAStack

# Convert decimal x (base 10) to base y

def convert_decimal(x, y):
    if type(x) != int or type(y) != int:
        raise TypeError('This function only works with integer input.')
    elif x < 0 or y <= 0 or y > 16: 
        raise ValueError('Invalid input.')
    print('In the base %d number system, decimal %d is considered as %s.' % (y, x, _convert_decimal(x, y)))
    
    c_stack = DSAStack.DSAStack()
    
    def convert2_string(x, y):
        convert_string = "0123456789ABCDEF"
        while x > 0:
            if x < y:
                c_stack.push(convert_string[x])
            else:
                c_stack.push(convert_string[x % y])
            x = x // y
        temp = ""
        while not c_stack.is_empty():
            temp += str(c_stack.pop())
        return temp

def _convert_decimal(x, y):
    
    rem = x % y

    if x <= 1:
        return str(x)
    else:
        return str(_convert_decimal(x//y, y)) + str(rem)
    
convert_decimal(678, 4)
