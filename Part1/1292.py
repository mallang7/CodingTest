#1292 - 쉽게 푸는 문제
n, m = map(int,input().split())
L=[]
sum=0
for i in range(1,46):
    for j in range(1,i+1):
        L.append(i)

for i in range(n-1,m):
    sum += L[i]
print(sum)