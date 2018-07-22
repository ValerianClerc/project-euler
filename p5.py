max = 20

current = max*(max-1)
for i in range(max-2, 9, -1):
    counter = 1
    tempCurr = current
    while current%i != 0:
        current = tempCurr*counter
        counter +=1
print(current)
