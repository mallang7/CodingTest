#4796번 - 캠핑
import sys
i=0
while True:
    L, P, V = map(int,sys.stdin.readline().split())
    if (L == 0):
        break
    i += 1
    day=(V//P)*L
    if (V%P) >= L:
        day += L
    else:
        day += V%P
    print("Case {}: {}".format(i,day))