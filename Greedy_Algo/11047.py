# 11047번 동전0
N, K = map(int,input().split())
N_list = []
for i in range(N):
    N_list.append(int(input()))
N_list.sort(reverse=True)
count = 0
for i in range(N):
    a = K // N_list[i]
    count = count+a
    K=K - a*N_list[i]
    if K ==0:
        break
print(count)