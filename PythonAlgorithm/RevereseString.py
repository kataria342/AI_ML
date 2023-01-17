import StackClass

string = "Learn a lot with linkedin Learning"

reversed_string = ""

s = StackClass.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)
