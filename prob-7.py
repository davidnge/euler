#What is the 10 001st prime number?

import math 

def isPrime(number):
    if number == 2:
       return True
    if number % 2 == 0:
        return False
    
    i = 3
    sqrtOfNumber = math.sqrt(number)
    
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2
        
    return True 

def main():
    n = 2
    count = 0
    while n > 0:
        if isPrime(n):
            count+=1
        if count == 10001:
            print n
            break
        n+=1

main()