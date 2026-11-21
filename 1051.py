n = int(input())
string=input()

if string.count(string[0]) == n:
    print(1)
    print(string)
else:
    arst = ("AB" * n)[0:n]

    print(2)
    print(arst)