list = []
# iterate through all numbers up to 1000
for i in range(1000):
    # if multiple of 3 or 5, add to list
    if i%3 == 0 or i%5 == 0:
        list.append(i)

# sum list
print(sum(list))
