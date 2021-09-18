T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    if A > 0 and B < 10 :
        print(A+B)
    else:
        print("A>0, B<10 인 값을 입력하세요")