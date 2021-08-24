import DSAHashTable

hashtest = DSAHashTable.DSAHashTable(1)

print("Add first element\nTable Size: 1 >> next prime >> 2\nLF = 1/2")
hashtest.put("90022616", "Kai")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")

print("Add second element\nTable Size: 2 >> next prime >> 5 # RESIZE 5*2 next prime >> 11 #\nLF = 2/11")
hashtest.put("90022617", "Yu")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")

print("Add third element\nTable Size: 11\nLF = 3/11")
hashtest.put("90022618", "L")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")

print("Add fourth element\nTable Size: 11\nLF = 4/11")
hashtest.put("90022619", "Yu")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")


hashtest.remove("90022616")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")
hashtest.remove("90022617")
print("Load factor of table is:", hashtest.get_load_factor(), "\n")