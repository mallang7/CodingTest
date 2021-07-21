# 14719번 - 빗물
H, W = map(int, input().split())
wall = list(map(int,input().split()))

rain = 0
for i in range(W):
    max_left = max(wall[:i+1])
    max_right = max(wall[i:])
    which_low = min(max_left,max_right)
    rain += abs(wall[i]-which_low)
print(rain)