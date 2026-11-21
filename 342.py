n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mxa = max(a)
mxb = max(b)

mia = min(a)
mib = min(b)

mylist = [mxa * mxb, mia * mib, mxa * mib, mxb * mia]

print(max(mylist))