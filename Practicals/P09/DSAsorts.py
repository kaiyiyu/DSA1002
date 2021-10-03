# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import numpy as np

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
    
    for i in range(len(A)):
        min_index = i
        
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
            
        temp = A[min_index]
        A[min_index] = A[i]
        A[i] = temp

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    right_index = len(A) - 1
    left_index = 0
    
    _mergeSortRecurse(A, left_index, right_index)

def _mergeSortRecurse(A, left_index, right_index):
    if left_index < right_index:
        mid_index = (left_index + right_index) / 2
        
        # Recurse left
        _mergeSortRecurse(A, left_index, mid_index)
        
        # Recurse right
        _mergeSortRecurse(A, mid_index + 1, right_index)
        
        _merge(A, left_index, mid_index, right_index)

def _merge(A, left_index, mid_index, right_index):
    array_len = right_index - left_index + 1
    temp_array = np.zeros(array_len, dtype=int)
    
    ii = left_index
    jj = mid_index + 1
    kk = 0
    
    while ii <= mid_index and jj <= right_index:
        if A[ii] <= A[jj]:
            temp_array[kk] = A[ii]
            ii += 1
        else:
            temp_array[kk] = A[jj]
            jj += 1
        kk += 1
        
    for ii in range(ii, mid_index + 1):
        temp_array[kk] = A[ii]
        kk += 1
        
    for jj in range(jj, right_index + 1):
        temp_array[kk] = A[jj]
        kk += 1
        
    for kk in range(left_index, right_index + 1):
        A[kk] = temp_array[kk - left_index] 

########## Quicksort Left-Most Pivot Selection ##########
def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    right_index = len(A) - 1
    left_index = 0
    
    _quickSortRecurse(A, left_index, right_index)

def _quickSortRecurse(A, left_index, right_index):
    if right_index > left_index:
        
        # Left-most pivot selection
        pivot_index = left_index
        new_pivot_index = _doPartitioning(A, left_index, right_index, pivot_index)
        
        # Recurse left
        _quickSortRecurse(A, left_index, new_pivot_index - 1)
        
        # Recurse right
        _quickSortRecurse(A, new_pivot_index + 1, right_index)

def _doPartitioning(A, left_index, right_index, pivot_index):
    pivot_value = A[pivot_index]
    A[pivot_index] = A[right_index]
    A[right_index] = pivot_value
    
    current_index = left_index
    
    for ii in range(left_index, right_index):
        if A[ii] < pivot_value:
            temp = A[ii]
            A[ii] = A[current_index]
            A[current_index] = temp
            current_index += 1
            
    new_pivot_index = current_index
    A[right_index] = A[new_pivot_index]
    A[new_pivot_index] = pivot_value
    
    return new_pivot_index

########## Quicksort Median of Three Selection ##########
def quickSortMedian3(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    right_index = len(A) - 1
    left_index = 0
    
    _quickSortMedian3Recurse(A, left_index, right_index)

def _quickSortMedian3Recurse(A, left_index, right_index):
    third_index = (left_index + right_index) / 2
    
    if right_index > left_index:
        
        # Median of three pivot selection
        pivot_index = _median3Pivot(A, left_index, right_index, third_index)
        new_pivot_index = _doPartitioning(A, left_index, right_index, pivot_index)
        
        # Recurse left
        _quickSortRecurse(A, left_index, new_pivot_index - 1)
        
        # Recurse right
        _quickSortRecurse(A, new_pivot_index + 1, right_index)

def _median3Pivot(A, i, j, k):
    if A[i] > A[j] and A[i] > A[k]:
        median = i
    elif A[j] > A[i] and A[j] > A[k]:
        median = j
    else:
        median = k
        
    return median

########## Three Way Quicksort ##########
def quickSort3Way(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    right_index = len(A) - 1
    left_index = 0
    
    _quickSort3WayRecurse(A, left_index, right_index)

def _quickSort3WayRecurse(A, left_index, right_index):
    i = 0
    j = 0
    if right_index >= left_index:
        
        # Three-way pivot selection
        _doPartitioning3(A, left_index, right_index, i, j)

        # Recurse left
        _quickSortRecurse(A, left_index, j)
        
        # Recurse right
        _quickSortRecurse(A, i, right_index)

def _doPartitioning3(A, left_index, right_index, i, j):
    if right_index - left_index <= 1:
        if A[right_index] < A[left_index]:
            _swap(A, right_index, left_index)
        i = left_index
        j = right_index
    else:
        mid = left_index
        pivot = A[right_index]
        
        while mid <= right_index:
            if A[mid] < pivot:
                _swap(A, left_index, mid)
                left_index += 1
                mid += 1
            elif A[mid] == pivot:
                mid += 1
            else:
                _swap(A, mid, right_index)
                right_index -= 1
        i = left_index - 1
        j = mid   

def _swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp