# 카펫 - 완전탐색
def solution(brown, yellow):
    answer = []
    div=[]
    m=0
    n=0
    if yellow==1:
        div.append(1)
    else:
        for i in range(1,yellow//2+1):
            if yellow % i ==0:
                div.append(i)
                div.append(yellow/i)
    div.sort()
    for j in range(len(div)-1,-1,-1):
        m=div[j]
        n=yellow/m
        if brown == 2*m+2*n+4:
            break
    answer.append(m+2)
    answer.append(n+2)
    return answer