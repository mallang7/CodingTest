# 음료수 얼려 먹기 149p
#n, m = map(int,input().split())
n=4
m=5

# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))
    
# print(graph)
graph = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def dfs(x,y):
    if x <= -1 or x> n or y <= -1 or y > n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)