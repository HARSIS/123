def f(a, b):
    c = ""
    while (a > 0):
        c = str(a % b) + c
        a = a // b
    return c
N = 2
while(N < 8):
    if (f(4646, N) + f(387, N + 2) == f(3746, N + 1)):
        print("@@@@@@@@")
        print(N)
    N += 1
print("@@@@@@@@")
print(N)