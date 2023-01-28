guestList = ["Raman", "Rahul", "Rajat"]

# Section 3-4: Inviting the guests
for i in guestList:
    print(i, ": You are invited for dinner.")

# Adding extra line
print()
print(guestList[1], "can not come for dinner")

# Section 3-5:Replacing Rahul with Rohit
guestList[1] = "Rohit"

# Adding extra line
print()
# Inviting the guests
for i in guestList:
    print(i, ": You are invited for dinner.")

# Section 3-6:Adding extra line
print()
print("I just found out that a bigger table is available, we can invite 3 more friends")

# Inserting at first position
guestList.insert(0, "Vinod")

# Inserting at middle position
guestList.insert(2, "Rohan")

# Inserting at last position
guestList.append("Shubham")

# Adding extra line
print()
# Inviting the guests
for i in guestList:
    print(i, ": You are invited for dinner.")

# Adding extra line
print()
print("I can only invite two person as there is some issues with table")

# Adding extra line
print()
# Section 3-7:removing guests from list
print( "Sorry", guestList.pop(), ", I am removing you because of table issue")
print( "Sorry", guestList.pop(), ", I am removing you because of table issue")
print( "Sorry", guestList.pop(), ", I am removing you because of table issue")
print( "Sorry", guestList.pop(), ", I am removing you because of table issue")

# Adding extra line
print()
# Inviting the guests
for i in guestList:
    print(i, ": You are still invited for dinner.")

# Deleting the list content
del guestList[0]
del guestList[0]
# Adding extra line
print()
print("Printing the updated guest list", guestList)

# Adding extra line
print()
# Section 3-8: Seeing the world
placesList = ["Morocco", "Switzerland", "New Zealand", "Australia", "Norway"]

# Printing the List
print("Original List:", placesList)
print("Alphabet Order list:", sorted(placesList))
print("Original List:", placesList)
print("Reverse Alphabet order:", sorted(placesList, reverse=True))
print("Original List:", placesList)
placesList.reverse()
print("Original list after reverse operation:", placesList)
placesList.reverse()
print("Original list:", placesList)
placesList.sort()
print("Alphabetically sorted list:", placesList)
placesList.sort(reverse=True)
print("Reverse Alphabetically sorted list:", placesList)

# Adding extra line
print()
# Section 3-9: dinner Guests
guestList = ["Raman", "Rahul", "Rajat"]

#  total Guest invited
print("Total", len(guestList)," guests are invited for dinner.")

# Adding extra line
print()
# Section 3-10: Every function
languageList = ["English", "French", "Russian", "Spanish", "Portuguese"]

# Adding one more language
languageList.append("Arabic")
print(languageList)
print(languageList.count("English"))
print(languageList.index("English"))
languageList.insert(0, "Urdu")
print(languageList)
print(languageList.pop())
languageList.remove("Russian")
print(languageList)
languageList.reverse()
print(languageList)
languageList.sort()
print(languageList)

# Adding extra line
print()
# Dictionary Practices
dictProgram = {
    "Python Programming": "Parwinder kaur",
    "Introduction to Artificial Intelligence": "Ashish Gupta",
    "Professional Communication": "Mahmoud Alqazli",
    "Big Fundamentals- Data Storage Networking":"Graham Wall",
    "Data Science and Machine Learning": "Amir Samiezadeh",
    "Careers in Artificial Intelligence and Machine Learning": "Muthanna Khishali"
}

print("Before Replacing:", dictProgram)
dictProgram["Big Fundamentals- Data Storage Networking"] = "Updated Name"
print("After Replacing", dictProgram)