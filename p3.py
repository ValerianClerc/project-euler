
primes = []

def findPrime(num):
    #iterate through all numbers until a gets to num (num shrinks during the loop's execution)
    for a in range(2,num):
        # if a has reached num, then the answer has been found
        if num <= a:
            print("ANSWER: " + str(a))
            break
        # otherwise, if the number is divisible by a, then num is divided by a and updated until it is <= a
        while num%a == 0:
            primes.append(a)
            num = num/a


findPrime(600851475143)
