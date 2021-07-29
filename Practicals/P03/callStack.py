import DSAStack

c_stack = DSAStack.DSAStack()

def convert2_string(x, y):
    convert_string = "0123456789ABCDEF"
    c_stack.push('convert2_string')
    c_stack.display()
    while x > 0:
        if x < y:
            c_stack.push(convert_string[x])
        else:
            c_stack.push(convert_string[x % y])
        x = x // y
        c_stack.display()
        
    while not c_stack.is_empty():
        c_stack.pop()
        c_stack.display()

convert2_string(16, 9)

