# 문자열 내 마음대로 정렬하기
def solution(strings, n):
    strings.sort()
    key_li = []
    value_li = []
    for i,v in enumerate(strings):
        key_li.append(i)
        value_li.append(v[n])
    dct = dict(zip(key_li,value_li))
    dct = dict(sorted(dct.items(),key=lambda x:x[1]))
    
    answer = []
    for i in dct.keys():
        answer.append(strings[i])
    return answer