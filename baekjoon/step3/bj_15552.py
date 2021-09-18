import sys

T = int(input())

if 0 <= T <= 1000000 :
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        if (1 <= A <= 1000 and 1 <= B <= 1000):
            print(A + B)
        else:
            print("A, B 값은 1에서 1,000 사이입니다.")
else:
    print("테스트케이스(T)의 값은 최대 1,000,000입니다.")