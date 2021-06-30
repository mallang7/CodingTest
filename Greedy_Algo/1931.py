# 1931번 - 회의실 배정
import sys
N = int(sys.stdin.readline())
L=[]
for _ in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))
L.sort(key=lambda x: (x[1],x[0]))

end=0
count=0
for i in range(N):
    if end <= L[i][0]:
        end = L[i][1]
        count += 1
print(count)