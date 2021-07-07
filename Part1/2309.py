# 2309 - 일곱난쟁이
import sys
L=[]
for _ in range(9):
    L.append(int(sys.stdin.readline()))
a=sum(L)
one=0
two=0
for i in range(8):
    for j in range(i+1,9):
        if (a - L[i] - L[j])== 100:
            one=L[i]
            two=L[j]
L.remove(one)
L.remove(two)
L.sort()
for i in L:
    print(i)