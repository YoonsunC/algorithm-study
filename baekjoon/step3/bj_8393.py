n = int(input())
hap = 0

if 1 <= n <= 10000:
    for i in range(1, n+1):
        hap = i + hap
    print(hap)
else:
    print("1부터 10,000까지의 값을 입력하세요")