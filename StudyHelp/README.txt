------------------------------------------------------------------------------
CURTIN COLLEGE - DIPLOMA OF INFORMATION TECHNOLOGY 
Assignment in Data Structures and Algorithms (DSA1002)
Trimester 2, 2021
------------------------------------------------------------------------------
CONTENTS

README.txt                - Readme file for DSA1002 Assignment
ProjectReport.pdf         - Documentation and Report for DSA1002 Assignment
StudyHelp.py              - Main file to run for StudyHelp program 
FileIO.py                 - File containing class for file handling 
DSALinkedList.py          - Implementation of doubly linked list ADT 
DSAHashTable.py           - Implementation of hash table ADT 
DSAQueue.py               - Implementation of queue ADT 
DSAGraph.py               - Implementation of graph ADT 
network.csv               - Network data file given for DSA1002 Assignment 
units.csv                 - Unit data file given for DSA1002 Assignment 
students.csv              - Student data file given for DSA1002 Assignment

Output Files
student.dat               - Serialized student data file 
network.dat               - Serialized network data file 
unit.dat                  - Serialized unit data file 
------------------------------------------------------------------------------
DEPENDENCIES 

FileIO.py                 - imports three CSV files, linked list, hash table, 
                            and graph ADT 
DSAGraph.py               - imports linked list and queue ADTs
DSAQueue.py               - imports linked list ADT
StudyHelp.py              - imports FileIO.py
------------------------------------------------------------------------------
HOW TO RUN PROGRAM

The StudyHelp program has three starting options.

[ python3 StudyHelp.py ]
    - output usage information of StudyHelp program

[ python3 StudyHelp.py -i ]
    - opens StudyHelp interactive mode

> As soon as the program starts, the user will be shown the menu and the user 
  will input a number from 1 to 8. Preferably, in the first run of the 
  program, all three data files should manually loaded. 

> After loading, any of the menu options can be chosen. It is also advisable 
  to serialize the data with option 8. If so, the next run of the program can
  load directly from the serialized data instead of manually loading the three
  CSV Files.
  
> For options 2 to 6, the user only needs to enter specified command input 
  when prompted. If the user is done with the program, simply return to the 
  menu and choose option 8.

[ python3 StudyHelp.py -r students.csv units.csv network.csv ]
    - opens StudyHelp report mode

> The program will automatically load all three data files and output network
  statistics once it is run.
-------------------------------------------------------------------------------