# 큰 수의 법칙 92p
# N,M,K = map(int,input().split())
# l = list(map(int,input().split()))
# l.sort()
# first = l[N-1]
# second = l[N-2]
# answer=0

# while(True):
#     for i in range(K):
#         if (M==0):
#             break
#         else:
#             answer += first
#             M -= 1
#     if(M==0):
#         break
#     else:
#         answer += second
#         M -= 1
    
# print(answer)

#더 간단한 방법
N,M,K = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
first = l[N-1]
second = l[N-2]
answer=0
answer += (M//(K+1))*K*first
answer += (M%(K+1)+M//(K+1))*second

print(answer)