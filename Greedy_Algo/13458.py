# 13458번 - 시험 감독
N = int(input())
A=list(map(int,input().split()))
B, C = map(int,input().split())
sum=0
for i in range(N):
    sum += 1
    if (A[i]>B):
        sum = sum + (A[i]-B)//C
        if (A[i]-B) % C !=0:
            sum = sum + 1
print(sum)