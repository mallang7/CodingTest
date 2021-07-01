# 1700번 - 멀티탭 스케줄링
import sys

def solution(Array):
    count=0
    Plugin = []
    for i in range(K):
        if Array[i] in Plugin:
            continue
        if len(Plugin) < N:
            Plugin.append(Array[i])
            continue
            
        count += 1
        out = 0
        outidx = 0
        
        for j in range(N):
            try:
                idx = Array[i+1:].index(Plugin[j])
                if idx > outidx:
                    out = j
                    outidx = idx
            except:
                out = j
                break
                
        Plugin[out] = Array[i]
    return count

N, K = map(int,sys.stdin.readline().split())
L=list(map(int,sys.stdin.readline().split()))
answer = solution(L)
print(answer)
