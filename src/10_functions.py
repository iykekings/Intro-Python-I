# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def my_function(num):
    if(num % 2 == 0):
        return True
    else:
        return False


# print(my_function(2))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if(my_function(num)):
    print('Even!')
else:
    print('Odd')

# YOUR CODE HERE
