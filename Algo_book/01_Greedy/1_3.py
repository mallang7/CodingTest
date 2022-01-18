# 숫자 카드 게임 96p
N, M = map(int,input().split())
data=[]
# for i in range(N):
#     data.append(list(map(int,input().split())))
l = []
for i in range(N):
    a = min(list(map(int,input().split())))
    l.append(a)
print(max(l))