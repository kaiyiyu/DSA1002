import time
import sys
import numpy as np

sys.setrecursionlimit(2000)

class Call_Stack:
    def _init_(self):
        ## We are first make the size of it. And the Dtype is list because we are storing the list.
        self.data = np.zeros(100, dtype=list)
        self.count = 0
        self.size = 100

    def get(self, i):
    ## It is stored at i th index
        return self.data[i]

    def append(self, iteam):
        self.data[self.count] = iteam
        self.count += 1

    def Push(self, val):
        self.append(val)

    def Pop(self):
        print(self.get(self.count -1))
        self.data[self.count -1] = 0
        self.count -=1


    def factorial(self, n):
        a = n
        self.Push("Factorail (self, n) Where n is %d"%(a))

        if n in [0, 1]:
            a = n
            print("Displaying the Stack")
            self.Display()
            return (1)
        print("Displaying the Stack")
        self.Display()
        return n * self.factorial(n-1)

    def Display(self):
        for i in self.data:
            if i == 0:
                break
            else:
                print(i)

d = Call_Stack()

print("Please enter the number: \n")
n = int(input())
start_time = time.time()

ans = d.factorial(n)
print("The factorial of %s is: %s"%(n, ans))
print("%s seconds"%(time.time()-start_time))