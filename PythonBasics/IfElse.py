"""
This Programs include If Else condition
"""
varA = int(input("Enter Value of A: "))
varB = int(input("Enter value of B: "))
varC = int(input("Enter value of C: "))
if varA > varB:
    if varA > varC:
        print("A is greater")
elif varB > varC:
    if varB > varA:
        print("B is greater")
else:
    print("C is greater")
