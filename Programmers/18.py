#21 카카오 - 메뉴리뉴얼
from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        temp=[]
        for order in orders:
            m=sorted(list(order))
            combi = combinations(m,i)
            for comb in combi:
                temp.append("".join(comb))
        count={}
        for t in temp:
            if t in count:
                count[t] +=1
            else:
                count[t]=1
        d=[k for k,v in count.items() if max(count.values())>1 and max(count.values())==v]
        for i in d:
            answer.append(i)
    return sorted(answer)