# 뉴스 클러스터링
from collections import Counter
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    A=[]
    B=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i:i+2])
        else:
            continue
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i:i+2])
        else:
            continue
    A.sort()
    B.sort()
    Counter1 = Counter(A)
    Counter2 = Counter(B)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    if len(A) == 0 and len(B)==0:
        answer = 65536
    else:
        answer = int(len(inter) / len(union) * 65536)
    return answer