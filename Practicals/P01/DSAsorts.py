#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#


def bubbleSort(array):
    
    pass_num = 0
    is_sorted = True
    
    while not is_sorted:
        for i in range(len(array) - 1 - pass_num) - 1:
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                is_sorted = False
        pass_num = pass_num - 1

an_array = [1, 9, 19, 7, 3, 10, 13, 15, 8, 12] 
bubbleSort(an_array)
print(an_array)

#def insertionSort(A):
#    ...
#
#def selectionSort(A):
#    ...


