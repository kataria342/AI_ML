a = int(input("Enter a: \n"))  # Global Variable


def helloworld():
    x = "Welcome to Canada"
    print(x)


helloworld()


def addition(e, f, g=1, h=2):  # Function with default parameter values
    b = int(input("Enter b: \n"))
    result = a + b + e + f + g + h
    print("Result is : ", result)
    return result   # Return value


addition(2, 3)
print("Return result", addition(2, 3, 4, 5))  # Function with Parameters
