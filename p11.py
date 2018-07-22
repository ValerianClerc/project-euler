def load():
    matrix = []
    f = open("p11.txt", "r")
    for i in range(0,20):
        temp = []
        for j in range(0,20):
            temp.append(f.read(2))
            f.read(1)
        matrix.append(temp)
    return matrix

def getMax(list):
    max = 0
    if len(list) >= 4:
        for i in range(0, len(list)-3):
            temp = int(list[i])*int(list[i+1])*int(list[i+2])*int(list[i+3])
            if temp >= max:
                max = temp
        return max
    else:
        return 0

def getUpDiag(grid):
    max = 0
    for i in range(0, 20):
        diag = []
        x = 0+i
        y = 0
        while x < 20 and y < 20:
            diag.append(grid[x][y])
            x = x + 1
            y = y + 1
        temp = getMax(diag)
        if temp >= max:
            max = temp
    for i in range(0, 20):
        diag = []
        x = 0
        y = 0+i
        while x < 20 and y < 20:
            diag.append(grid[x][y])
            x = x + 1
            y = y + 1
        temp = getMax(diag)
        if temp >= max:
            max = temp
    return max

def getDownDiag(grid):
    max = 0
    for i in range(0, 20):
        diag = []
        x = 0+i
        y = 19
        while x < 20 and y >= 0:
            diag.append(grid[x][y])
            x = x + 1
            y = y - 1
        temp = getMax(diag)
        if temp >= max:
            max = temp
    for i in range(0, 20):
        diag = []
        x = 0
        y = 19-i
        while x <20 and y >=0:
            diag.append(grid[x][y])
            x = x + 1
            y = y - 1
        temp = getMax(diag)
        if temp >= max:
            max = temp
    return max

grid = load()

max = 0

#rows
for i in range(0,20):
    temp = getMax(grid[i])
    if temp >= max:
        max = temp

#columns
for i in range(0, 20):
    temp = getMax(grid[i])
    if temp >= max:
        max = temp

#upDiag
temp = getUpDiag(grid)
if temp >= max:
    max = temp

#downDiag
temp = getDownDiag(grid)
if temp >= max:
    max = temp

print(max)
