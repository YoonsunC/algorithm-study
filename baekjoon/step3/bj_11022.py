T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    if A > 0 and B < 10:
        print("Case #", i, ": ", A, " + ", B, " = ", A+B, sep='')
    else:
        print("A > 0, B < 10을 만족하는 값을 입력하세요")

