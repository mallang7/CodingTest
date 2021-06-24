# 11399번 - ATM
N = int(input())
P = list(map(int,input().split()))
P.sort()
sum = 0
for i in range(N):
    for j in range(0,i+1):
        sum = sum + P[j]
print(sum)