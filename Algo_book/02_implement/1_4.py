# 게임 개발 118p
N,M=map(int,input().split())
x,y,direction = map(int,input().split())
datas=[]
for i in range(M):
    datas.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

#1단계
def turn_left():
    global direction
    direction -= 1
    if direction== -1:
        direction= 3

count=1
turn_time=0
while True:
    # 1단계
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    if datas[nx][ny] == 0:
        datas[x][y]=1
        x = nx
        y = ny
        count +=1
        turn_time=0
        continue
    else:
        turn_time += 1
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        if datas[nx][ny] == 0:
            x =nx
            y= ny
        else:
            break
        turn_time=0
        
print(count)