def p9():
    for a in range(1000,1,-1):
        for b in range(1000, a, -1):
            if a+b < 1000:
                for c in range(1000, b, -1):
                    if a+b+c == 1000 and a**2+b**2==c**2:
                        print("a" + str(a))
                        print("b" + str(b))
                        print("c" + str(c))
                        return 0

p9()
