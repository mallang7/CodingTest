# 1978 - 소수 찾기
N = int(input())
L=list(map(int,input().split()))
count=0
for i in range(N):
    S=[]
    for j in range(1,L[i]+1):
        if L[i] % j ==0:
            S.append(i)
    if len(S) == 2:
        count += 1
print(count)