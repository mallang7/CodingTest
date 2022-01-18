# 1이 될 때까지 99p
# N, K = map(int,input().split())
# count=0
# while True:
#     if N==1:
#         break
#     else:
#         if N%K == 0:
#             N = N / K
#         else:
#             N -= 1
#     count += 1
            
# print(count)

# K=1인 경우까지 생각했을 때(모범답안)
N, K = map(int,input().split())
count = 0

while N >= K:
    while N%K != 0:
        N -= 1
        count += 1
    N = N//K
    count += 1

while N > 1:
    N -= 1
    count += 1

print(count)