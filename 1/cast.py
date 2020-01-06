#Write a program that reads an integer number and prints its previous and next numbers. See the examples #below for the exact format your answers should take. There shouldn't be a space before the period.
#Remember that you can convert the numbers to strings using the function str.

# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)

num = (input())
n = int(num)
next = n + 1
prev = n - 1
print("The next number for the number " + num + " is " + str(next) + ".")
print("The previous number for the number " + num + " is " + str(prev) + ".")