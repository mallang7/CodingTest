# 12845번 - 모두의 마블
# import sys
# N = int(sys.stdin.readline())
# A=list(map(int,sys.stdin.readline().split()))
# gold=0
# for i in range(N-2):
#     M = max(A)
#     m = A.index(M)
#     if (m!=len(A)):
#         b = A.index(max(A[m-1],A[m+1]))
#     else:
#         b = m-1
#     gold += (M+A[b])
#     del A[b]
# print(gold)

import sys
N = int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
gold=sum(A)+max(A)*(N-2)
print(gold)