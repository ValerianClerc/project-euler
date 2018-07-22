evenFibs = []
a = 0
b = 1
# iterate until larger number reaches 4000000
while b < 4000000:
    # if this fibonacci number is even, add to list
    if (a+b)%2 ==0:
        evenFibs.append(a+b)

    # increment fibonacci numbers, keeping b as the larger
    temp = a+b
    a = b
    b = temp

# sum list of even fibonacci numbers
print("ANSWER: " + str(sum(evenFibs)))
