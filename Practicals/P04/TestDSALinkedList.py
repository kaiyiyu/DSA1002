import DSALinkedList
import pickle

new_list = DSALinkedList.DSALinkedList()

# Test insert_first method
print("After insert_first()...")
new_list.insert_first(9)
new_list.insert_first(16)
for item in new_list:
    print(item)

# Test insert_last method
print("\nAfter insert_last()...")
new_list.insert_last("DSA")
new_list.insert_last(10.2)
for item in new_list:
    print(item)

# Test remove_first method
print("\nAfter remove_first()...")
new_list.remove_first()
for item in new_list:
    print(item)
    
# Test remove_last method
print("\nAfter remove_last()...")
new_list.remove_last()
for item in new_list:
    print(item)

# Test peek_first method
print("\nAfter peek_first()...")
print(new_list.peek_first())

# Test peek_last method
print("\nAfter peek_last()...")
print(new_list.peek_last())

# Serialization
print("\nSaving object to file...")
try:
    with open("linkedlist.dat", "wb") as dataFile:
        pickle.dump(new_list, dataFile)
except:
    print("\nError: Problem pickling object!")

#Deserialization
with open("linkedlist.dat", "rb") as dataFile:
    elements = pickle.load(dataFile)

    print("\nLoading list in file...")
    for element in elements:
        print(f"An element is: {element}")
