# 10818 - 최소,최대
N=int(input())
L=list(map(int,input().split()))
min=max=L[0]
for i in range(N):
    if min>=L[i]:
        min = L[i]
    if max<=L[i]:
        max = L[i]
print('{} {}'.format(min,max))