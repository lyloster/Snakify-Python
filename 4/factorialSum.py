# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop,
# so try to discover it. And don't use the math library :)

def sum():
	n = int(input())
	sum = 0
	for num in range (1, n+1):
		sum += factorial(num)
	print(sum)

def factorial(n):
	factorial = 1
	for num in range(1, n+1):
		# print("factorial ", factorial, " num ", num)
		factorial *= num 
	return factorial


sum()
