#1946번 - 신입 사원
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    A=[]
    count = 1
    
    N=int(input())
    for _ in range(N):
        Paper, Interview = map(int,sys.stdin.readline().split())
        A.append([Paper, Interview])
        
    A.sort()
    max = A[0][1]
    for i in range(1,N):
        if max > A[i][1]:
            count += 1
            max = A[i][1]
    print(count)