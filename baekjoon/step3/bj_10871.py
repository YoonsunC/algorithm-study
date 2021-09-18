N, X = map(int, input().split())
A = []
val = int(input().split())

if (1 <= N <= 10000 and 1 <= X <= 10000):
    for i in range(N):
        A.append(val)
    for j in A:
        if j < X:
            print(j, end='')
else:
    print("1부터 10000 사이의 값을 입력하세요")