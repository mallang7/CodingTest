# 2501 - 약수 구하기
N, K = map(int,input().split())
ans=[]
for i in range(1,N+1):
    if N % i == 0:
        ans.append(i)

if len(ans)<K:
    print(0)
else:
    print(ans[K-1])