#1969번 - dna
N, M = map(int,input().split())
L = []
for _ in range(N):
    L.append(input())

answer=[]
result=0
dna=['A','C','G','T']

for i in range(M):
    b=[0,0,0,0]
    line=[]
    count=0
    maxi=''
    for j in range(N):
        if L[j][i] == dna[0]:
            b[0] += 1
        elif L[j][i] == dna[1]:
            b[1] += 1
        elif L[j][i] == dna[2]:
            b[2] += 1
        else:
            b[3] += 1
        line.append(L[j][i])
        
    maxi=dna[b.index(max(b))]
    answer.append(str(maxi))
    count = N - line.count(maxi)
    result += count

print(''.join(answer))
print(result)