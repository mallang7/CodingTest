# 2019 카카오 - 징검다리
def solution(stones, k):
    answer = 0
    jump=0
    while ((jump+2) <= k):
        answer += 1
        jump=0
        idx=[]
        for i in range(len(stones)):
            if stones[i] != 0:
                stones[i] -= 1
        for j in range(len(stones)-1):
            if stones[j]==0 and stones[j+1]==0:
                jump+=1
                idx.append(jump)
            else:
                jump=0
                idx.append(jump)
        jump = max(idx)
    return answer

#테케1,2 실패