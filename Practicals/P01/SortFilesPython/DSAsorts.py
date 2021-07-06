#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

##### File Reading: One Line at a Time (from Lecture) #####

def readFile(filename):
    try:
        fileObj = open(filename)

        lineNum = 0
        line = fileObj.readline()

        while line:
            lineNum += lineNum
            processLine(line)
            line = fileObj.readline()

        fileObj.close()

    except IOError as e:
        print("Error in file processing: " + str(e))

def bubbleSort(A):
    ...

def insertionSort(A):
    ...

def selectionSort(A):
    ...


