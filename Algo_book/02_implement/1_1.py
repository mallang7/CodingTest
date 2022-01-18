# 구현 - 1. 상하좌우
N = int(input())
datas=list(input().split())
x=1
y=1
for data in datas:
    if(data=='L'):
        if (y-1 != 0):
            y -= 1
    elif(data=='R'):
        if (y+1 != N):
            y += 1
    elif(data=='U'):
        if (x-1 != 0):
            x -= 1
    else: #data==D
        if (x+1 != N):
            x += 1
print('{} {}'.format(x,y))