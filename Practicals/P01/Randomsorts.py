#
# Python File I/O - code from lecture slides
#

##### File Reading #####
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

##### Manual Parsing of Known-Format CSV Row #####
def processLine(csvRow):

    tokens = csvRow.split(",")

    try:
        id = (tokens[0])
        name = tokens[1]
        
        print(" ID:" + id + " Name:" + name)

    except TypeError:
        raise TypeError("CSV row had invalid format")

##### try
readFile('RandomNames7000.csv')
