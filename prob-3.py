import math
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def isPrime(number):
    if number == 2:
       return true
    if number % 2 == 0:
        return False
    
    i = 3
    sqrtOfNumber = math.sqrt(number)
    
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2
        
    return True 


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def compute(n):
	
	a = factors(n)
	prime = []
	for i in a:
		if isPrime(i):
			prime.append(i)
	print prime

		

compute(600851475143)






		

