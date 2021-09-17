H, M = map(int, input().split())
early = M-45

if early < 0:
    H = H-1
    M = early + 60
else:
    M = early
if H < 0:
    H = H + 24
print(H, M)