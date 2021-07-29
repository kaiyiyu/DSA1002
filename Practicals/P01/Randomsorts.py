import csv
import DSAsorts

class FileSorter:
    
    listToSort = []

    def __init__(self, sortType):
        self.sortType = sortType

    def readFile(self, inFile):   
        with open(inFile,'r') as inputFile:
            reader = csv.reader(inputFile)

            for row in reader:
                rowStr = int(row[0])
                self.listToSort.append(rowStr)
                
        if self.sortType == 'Bubble':
            DSAsorts.bubbleSort(self.listToSort)
            self.saveFile('Bubble.csv')
        elif self.sortType == 'Selection':
            DSAsorts.selectionSort(self.listToSort)
            self.saveFile('Selection.csv')
        elif self.sortType == 'Insertion':
            DSAsorts.insertionSort(self.listToSort)
            self.saveFile('Insertion.csv')
                
    def saveFile(self, outFile):
        
        outputFile = open(outFile, 'w')
        
        for index in self.listToSort:
            outputFile.write(str(index) + '\n')
        
        outputFile.close()
    
