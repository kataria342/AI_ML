dictA = {"Name": "Prabhjeet", "Program":"AIML", "Subject": "PythonProgramming"}

# Print Type
print(type(dictA))

# Print full dictionary
print(dictA)

# Print value of key
print(dictA["Name"])

# Print Keys
print("dictionary Keys:", dictA.keys())

# Print Values
print("dictionary values:", dictA.values())

# Change Value
dictA["Name"] = "Pawan"
print(dictA)

# Add new key-value
dictA["Term"] = "Winter2023"
print(dictA)

# Remove the pair
dictA.pop("Term")
print(dictA)

# Traverse using for loop
for i in dictA:
    print(dictA[i])

# copying the dict
newDictB = dictA.copy()
print(newDictB)
newDictB.clear()
print(dictA)
print(newDictB)

# copying the dict using assignment
newDictC = dictA
print(newDictC)
newDictC.clear()
print(dictA)
print(newDictC)