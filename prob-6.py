#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def main(n):
	sumSquare = 0
	squareSum = 0
	for i in range(1,n+1):
		sumSquare += i**2
		squareSum += i
	squareSum**=2

	diff = abs(squareSum - sumSquare)
	print diff


main(100)