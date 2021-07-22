import DSAStack

def call_stack(n, base):
    c_stack = DSAStack.DSAStack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            c_stack.push(convert_string[n])
        else:
            c_stack.push(convert_string[n % base])
        n = n // base
        temp = ""
    
    while not c_stack.is_empty():
        temp = temp + str(c_stack.pop())
    return temp
print(call_stack(1453, 16))