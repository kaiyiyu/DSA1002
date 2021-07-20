import DSAStack

# Test stack class here

stacked = DSAStack.DSAStack()

# test push and pop methods -- if push() works properly then is_full works too
stacked.push('1')
stacked.push(0)
stacked.push(0)
stacked.push(2.0)    
print('The current items in the stack are:')
for i in range(stacked.count):
    print(stacked.get_count(i))
    
stacked.pop()
stacked.pop()

print('\nAfter two pops, the remaining items in the stack are:')
for i in range(stacked.count):
    print(stacked.get_count(i))
    

# test top() -- if top() works properly then is_empty works too
print('\nThe current top item is:', stacked.top())
