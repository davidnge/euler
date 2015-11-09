#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime(divisible_list):
	prime = []
	for num in divisible_list:
		if is_prime(num):
			prime.append(num)
	print prime[-1]

def get_divisible(n):
	
	is_divisible = []
	start = 2
	for i in range(start,n):
		if n%i==0:
			is_divisible.append(i)

	get_prime(is_divisible)

get_divisible(600851475143)
			






		

