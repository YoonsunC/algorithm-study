N = int(input())
A = int(N / 10)
B = int(N % 10)
C = A*10 + B
origin = C
cycle = 0

if 0 <= N <= 99:
    while (A/10) != B:
       
        A = int(C / 10)
        B = C % 10

        fir = B
        sec = int((A + B) % 10)
        C = (fir * 10) + sec
        cycle = cycle + 1
        if origin == C:
            break

    print(cycle)

else:
    print("0부터 99 사이의 값을 입력하세요")