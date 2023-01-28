a = int(input("Enter a: \n"))  # Global Variable


def helloworld():
    x = "Welcome to Canada"
    print(x)


helloworld()


def addition(e=1, j=1): # Function with default parameter values
    b = int(input("Enter b: \n"))
    result = a + b
    print("Result is : ", result)
    result = a + b + e + j
    print("Result is : ", result)


addition()
addition(2, 3) # Function with Parameters
