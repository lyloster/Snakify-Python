#NOTE! Off by one

# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop,
# so try to discover it. And don't use the math library :)

def sum():
	n = int(input())
	sum = 0
	for num in range (n+1):
		sum += factorial(num)
	print(sum)

def factorial(n):
	factorial = 1
	for num in range(n, 0, -1):
		# print("factorial ", factorial, " num ", num)
		factorial = factorial * num 
	return factorial


sum()
