# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def numEven(n):
    if n % 2 == 0:
        print(True)
    else: 
        print(False)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
numEven(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def numEven2(n):
    if n % 2 == 0:
        print("Even!")
    else: 
        print("Odd")

num1 = input("Enter a number: ")
num1 = int(num1)
numEven2(num1)