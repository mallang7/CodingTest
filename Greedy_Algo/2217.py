#2217번 - 로프
N=int(input())
P=[]
for _ in range(N):
    P.append(int(input()))
P.sort(reverse=True)
for i in range(N):
    P[i] = P[i] * (i+1)
print(max(P))