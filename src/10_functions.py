def mult2(n):
    return n * 2

num = 50

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2

nums = [10, 60, 4, 15]

def mult2_new_list(l):
    new_list = []

    for i in range(len(l)):
        new_list.append(l[i] * 2)

    return new_list

print(mult2(num))

print("------------------------")

mult2_list(nums)
print(nums)

print("------------------------")

print(mult2_new_list([3, 5, 34, 10, 15]))

  
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