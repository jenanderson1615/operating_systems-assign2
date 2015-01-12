#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework2
#Question4 

import sys
import math

numOfPrimes = int(sys.argv[1])
primeArray = []

#This function returns 1 if x is prime and 0 if x is not prime
def isPrime(x):
	if x == 2 or x == 3:
		return int(1)
	if x%2 == 0:
		return int(0)
	if x%3 == 0:
		return int(0)
	maxToCheck = math.ceil(math.sqrt(x))
	i = 4
	while i <= maxToCheck:
		if x % i == 0:
			return int(0)
		i += 1	
	return int(1)

x = 2
lengthOfArray = len(primeArray)

while (lengthOfArray < numOfPrimes):
	if isPrime(x) == 1:
		primeArray.append(x)
		lengthOfArray += 1
	x += 1
print primeArray[numOfPrimes - 1]
