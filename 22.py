n = int(input())
t = list(map(int, input().split()))

if n <= 1:
    print("Yes")
    exit()

result = "Yes"
temp = t[1] - t[0]

for i in range(n-1):
    if temp != t[i+1] - t[i]:
        result = "No"

print(result)