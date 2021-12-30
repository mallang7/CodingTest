from itertools import combinations
N = int(input())
bridge=[]
for i in range(N):
    bridge.append(list(map(int,input().split())))
    
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def solution(list):
    res = []
    for i in list:
        res.append(factorial(i[1]) // (factorial(i[1]-i[0])*(factorial(i[0]))))
    return res

answer = solution(bridge)
for i in range(N):
    print(answer[i])
