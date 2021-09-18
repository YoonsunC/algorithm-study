N = int(input())

if 1 <= N <= 100:
    for i in range(1, N+1):
        print("*" * i)
else:
    print("1 부터 100까지의 값을 입력하세요")