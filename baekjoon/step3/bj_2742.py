N = int(input())

if 1 <= N <= 100000:
    for i in range(N):
        print(N-i)
else:
    print("100,000보다 작거나 같은 자연수를 입력하세요")