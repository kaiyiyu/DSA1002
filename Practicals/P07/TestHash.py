import DSAHashTable

def printDivider():
        print("----------------------------------------------------")  
        
hashtest = DSAHashTable.DSAHashTable(4)

hashtest.put("90022616", "MajesticSeaLion")
print("LF:", hashtest.get_load_factor())
printDivider()

hashtest.put("90022617", "InsecureLizard")
print("LF:", hashtest.get_load_factor())
printDivider()

hashtest.put("90022618", "HarmlessKitten")
print("LF:", hashtest.get_load_factor())
printDivider()

hashtest.put("90022619", "GlitteringApricot")
print("LF:", hashtest.get_load_factor())
printDivider()

hashtest.remove("90022616")
print("LF:", hashtest.get_load_factor())
printDivider()

hashtest.remove("90022617")
print("LF:", hashtest.get_load_factor())
printDivider()

print("Expected value: GlitteringApricot\nProgram output:", hashtest.get("90022619"))