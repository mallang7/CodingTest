N, S = map(int,input().split())
L = list(map(int,input().split()))
min_length = N+1
start, end = 0, 0
tmp_sum = 0

while True:
    if tmp_sum >= S:
        min_length=min(min_length,end-start)
        tmp_sum -= L[start]
        start += 1
    elif end == N:
        break
    else:
        tmp_sum += L[end]
        end += 1
            
if min_length == (N+1):
    print(0)
else:
    print(min_length)