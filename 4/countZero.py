# Given N numbers: the first number in the input is N, 
# after that N integers are given. Count the number of 
# zeros among the given integers and print it.
# You need to count the number of numbers that are equal
# to zero, not the number of zero digits.

count = 0 
n = int(input()) + 1
for num in range(n):
    temp = int(input())
    if temp == 0:
        count = count + 1
        
print(count)