aarst = 0

for i in range(int(input())):
    h, f = input().split()
    if int(h) == 1 and int(f) == 0:
        aarst += 1

print(aarst)