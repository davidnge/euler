#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# this solution takes 1 minute to populate the answer

def find_smallest():
	smallest=1
	while smallest > 0:
		for num in range (1,21):
			if smallest%num!=0:
				break
			if num==20 and smallest%num==0:
				return smallest
		
		smallest+=1	

	
small = find_smallest()
print small