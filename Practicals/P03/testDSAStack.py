import DSAStack

# Driver code

stack = DSAStack.DSAStack()

# test push and pop methods -- if push() works properly then is_full works too
stack.push('1')
stack.push(0)
stack.push(0)
stack.push(2.0)    
print('The current items in the stack are:')
for i in range(stack.count):
    print(stack.get_count(i))
    
stack.pop()
stack.pop()

print('\nAfter two pops, the remaining items in the stack are:')
for i in range(stack.count):
    print(stack.get_count(i))
    

# test top() -- if top() works properly then is_empty works too
print('\nThe current top item is:', stack.top())

    