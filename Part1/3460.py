# 3460 - 이진수
for _ in range(int(input())):
    n = int(input())
    i = 0
    while n > 0:
        if n%2 == 1:
            print(i, end=' ')
        n = n//2
        i += 1

# T = int(input())
# L=[]
# for _ in range(T):
#     L.append(int(input()))

# Ref=[i for i in range(0,20)]

# for i in range(T):
#     ans=[]
#     for j in range(len(Ref),0,-1):
#         if L[i] >= 2**Ref[j]:
#             ans.append(j)
#             L[i] = L[i] - 2**Ref[j]
#     print(reversed(ans))