#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
	if str(n)==str(n)[::-1]:
		return True
	else:
		return False


def main():
	palinList = []
	MAX = 999
	for i in range(0,MAX):
		for m in range(0,MAX):
			prod = i*m
			if isPalindrome(prod):
				palinList.append(prod)
	print max(palinList)


main()






