def collatz(len, n):
    len=len+1
    if n == 1:
        return len
    if n%2 == 0:
        n=n/2
        return collatz(len, n)
    else:
        n=3*n+1
        return collatz(len, n)
max = 0
for i in range(1000000, 1, -1):
    curr = collatz(0, i)
    if curr >= max:
        max = curr
        if max >= 500:
            print(str(max) + " and " + str(i))
