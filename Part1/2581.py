# 2581 - 소수
M=int(input())
N=int(input())
ans=[]
for i in range(M,N+1):
    L=[]
    for j in range(1,i+1):
        if i % j ==0:
            L.append(j)
        if len(L) >3:
            break
    if len(L)==2:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
    