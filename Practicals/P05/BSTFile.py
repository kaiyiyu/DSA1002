import DSABinarySearchTree
import csv
import pickle

new_bst = DSABinarySearchTree.DSABinarySearchTree()

# Reading and writing CSV File
with open("RandomNames.csv",'r') as inputFile:
    reader = csv.reader(inputFile)
    for row in reader:
        new_bst.insert(row[0], row[1])

with open("traversal.csv", "w") as outFile:
    user_input = input("Select traversal:\n[1] Preorder\n[2] Inorder\n[3] Postorder\n")
    if user_input == "1":
        tree = new_bst.traverse_preorder()
    elif user_input == "2":
        tree = new_bst.traverse_inorder()
    elif user_input == "3":
        tree = new_bst.traverse_postorder()
    else:
        raise Exception("Invalid input: %s" % user_input)
    
    for index in tree:
        outFile.write("Student Name: " + str(index) + "\n")

# Reading and writing a serialized file with inorder data
print("\n### Saving object to file ###\n")
try:
    with open("bst.dat", "wb") as dataFile:
        pickle.dump(new_bst, dataFile)
except:
    print("\nError: Problem pickling object!")
    
with open("bst.dat", "rb") as dataFile:
    print("\n### Writing data to file ###")
    elements = pickle.load(dataFile)

    with open("deserialized.txt", "w") as outFile:
        for element in elements:    
            outFile.write("Student Data: " + str(element) + "\n")

# Display tree 
print("\n### Displaying inorder traversal ###")
new_bst.display()


    
