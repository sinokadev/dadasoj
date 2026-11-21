for i in range(int(input())):
    n, p = input().split()
    print("P is NP!" if int(p)*int(n) == int(p) else "P is not NP!")