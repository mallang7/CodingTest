# 5번 볼링공 고르기(315p)
from itertools import combinations
N, M = map(int,input().split())
weight = list(map(int,input().split()))
weight.sort()
result = len(list(combinations(weight,2)))
print(result)
count = 1
for i in range(1,len(weight)):
    if weight[i] == weight[i-1]:
        count += 1
    elif count >= 2:
        result -= len(list(combinations(count,2)))
        count = 1
    else:
        continue

print(result)