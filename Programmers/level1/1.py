# 예산
def solution(d, budget):
    answer = 0
    d.sort()
    if sum(d) <= budget:
        return len(d)
    if d[0] > budget:
        return 0
    for i in range(len(d)-1,-1,-1):
        if sum(d[0:i]) <= budget:
            return i
    return answer