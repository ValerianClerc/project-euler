
def sieve():
    n = 2000001
    dict = {}
    for i in range(2, n):
        dict[i] = "u"
    for p in range(2, n):
        count = p
        mult = 2
        while count < n:
            count = mult*p
            dict[count] = "m"
            mult = mult +1
    ans = []
    for i in range(2, n):
        if(dict[i] == "u"):
            ans.append(i)
    print(sum(ans))
sieve()

# def sieve2():
#     n = 2000001
#     list = []
#     for i in range(2, n):
#         list.append(True)
#     for p in range(2, n):
#         count = p
#         mult = 2
#         while count < n:
#             count = mult*p
#             list[count] = False
#             mult = mult + 1
#     ans = []
#     for i in range(2,n):
#         if(list[i]):
#             ans.append(i)
#     print(sum(ans))
#
# sieve2()
