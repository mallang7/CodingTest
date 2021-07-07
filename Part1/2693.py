# 2693 - N번째 큰 수
import sys
T = int(sys.stdin.readline())
L=[]
S=[]
for _ in range(T):
    L.append(list(map(int,sys.stdin.readline().split())))
for i in range(T):
    S = L[i]
    S.sort()
    print(S[7])