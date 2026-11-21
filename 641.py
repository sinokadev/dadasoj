n, m, k = map(int, input().split())
a = list(map(int, input().split()))

result = []

for i in range(k):
    asdfa = [i+1] * a[i]
    result += asdfa

# result를 sum(a)/n개 여러개로 자르고
# 짝수번째거를 뒤집어서 출력하면 되는거 아님?

asdfasd = n*m//(sum(a)//n)
ssss = sum(a)//n

for i in range(asdfasd):
    ads = result[ssss*i:ssss*i+ssss]
    if i%2 == 0:
        print(*ads)
    else:
        print(*ads[::-1])