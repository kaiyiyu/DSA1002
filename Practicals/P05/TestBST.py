import DSABinarySearchTree

bst = DSABinarySearchTree.DSABinarySearchTree()

# Test insert() and display()
print("Inserting keys and values...")
bst.insert(50, "50")
bst.insert(16, "16")
bst.insert(7, "7")
bst.insert(89, "89")
bst.insert(70, "70")
bst.insert(45, "45")
bst.insert(10, "10")
bst.insert(66, "66")
bst.insert(95, "95")
bst.display()

# Test calc_min()
print("\nTest calc_min()...")
print(bst.calc_min())

# Test calc_max()
print("\nTest calc_max()...")
print(bst.calc_max())

# Test height()
print("\nTest height()...")
print(bst.height())

# Test traverse_inorder()
print("\nTest traverse_inorder()...")
inorder = bst.traverse_inorder()
for i in inorder:
    print(i)

# Test traverse_preorder()
print("\nTest traverse_preorder()...")
preorder = bst.traverse_preorder()
for i in preorder:
    print(i)

# Test traverse_postorder()
print("\nTest traverse_postorder()...")
postorder = bst.traverse_postorder()
for i in postorder:
    print(i)

# Test balance()
print("\nTest balance()...")
print(bst.balance())

# Test delete()
print("\nTest delete()...")
bst.delete(50)
bst.display()

# Test find()
print("\nTest find()...")
print(bst.find(66))
