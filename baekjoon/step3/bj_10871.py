N, X = map(int, input().split())
A = list(map(int, input().split()))

if (1 <= N <= 10000 and 1 <= X <= 10000):
    for i in range(N):
        if (A[i] < X): 
            print(A[i], end=" ")
        else:
            pass
else:
    print("1부터 10000 사이의 값을 입력하세요")