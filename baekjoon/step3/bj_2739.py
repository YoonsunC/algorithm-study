N = int(input())

if 1 <= N <= 9 :
    for i in range(1, 10):
        print(N, "*", i, "=", N*i)
else:
    print("1부터 9까지의 값을 입력하세요")