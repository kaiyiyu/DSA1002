#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#


def bubbleSort(A):
    
    pass_num = 0
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        for i in range(len(A) - 1 - pass_num):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp
                is_sorted = False
            
    pass_num += 1

def insertionSort(A):

    for i in range(1, len(A)):
        j = i 
        
        temp = A[j]
        while j > 0 and A[j-1] > temp:
            A[j] = A[j-1]
            j -= 1
            
        A[j] = temp

def selectionSort(A):
    
    for i in range(0, len(A) - 1):
        min_index = i
        
        for j in range(i + 1, len(A) - 1):
            if A[j] < A[min_index]:
                min_index = j
            
        temp = A[min_index]
        A[min_index] = A[i]
        A[i] = temp
