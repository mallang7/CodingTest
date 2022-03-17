# H-index
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)-1,-1,-1):
        cnt_less = 0
        cnt_bigger = 0
        h=i+1
        for j in citations:
            if j<=h:
                cnt_less += 1
            if j>=h:
                cnt_bigger += 1
        if cnt_bigger>=h and cnt_less<=h:
            answer = h
            break
    return answer