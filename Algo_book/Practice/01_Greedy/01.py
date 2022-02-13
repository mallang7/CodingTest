# 그리디 01. 모험가 길드 (311p)
n = int(input())
adventure = list(map(int,input().split()))

adventure.sort()
result = 0 #답
count = 0 #현재 그룹에 포함된 모험가 수

for i in adventure:
    count += 1
    if i >= count:
        result += 1
        count = 0

print(result)