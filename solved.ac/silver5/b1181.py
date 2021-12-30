import sys
N = int(sys.stdin.readline())
l=[]
l=list(set(str(sys.stdin.readline().strip()) for _ in range(N)))

l.sort()
l.sort(key=len)

for i in l:
    print(i)