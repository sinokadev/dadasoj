tmp = 1234

n = int(input())
i = 0

while tmp != 0:
    i+=1
    tmp = 6*i%n

print(i)