n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(1, n):
    if a[i-1] == a[i]:
        count += 1

if count >= 2:
    print(0)
elif count == 1:
    print(2)
elif count == 0:
    print(n+3)