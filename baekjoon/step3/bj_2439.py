N = int(input())

if 1 <= N <= 100:
    for i in range(1, N+1):
        print(" "*(N-i), "*"*i, sep='')
else:
    print("1부터 100까지의 수를 입력하세요")