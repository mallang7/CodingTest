# 2460 - 지능형 기차 2
L=[]
for _ in range(10):
    L.append(list(map(int,input().split())))

ans=[]
people=0
for i in range(10):
    people -= L[i][0]
    people += L[i][1]
    ans.append(people)
    
print(max(ans))