primes = []
i=2
while(len(primes) < 10002):
    bool = 0
    for j in range(1, len(primes)):
        if i%primes[j] == 0:
            bool = 1
            break
    if bool == 0:
        primes.append(i)
    i = i+1

print(primes[len(primes)-1])
