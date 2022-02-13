# 그리디 01. 모험가 길드 (311p)
n = int(input())
adventure = list(map(int,input().split()))

adventure.sort()
count = 0
while adventure:
    out = adventure[-1]
    del adventure[-1]
    
    for i in range(out-1):
        del adventure[0]
    count += 1
print(count)