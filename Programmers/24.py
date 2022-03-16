# 정렬 -K번째 수
def solution(array, commands):
    answer = []
    for l in commands:
        array2 = array[(l[0]-1):(l[1])]
        array2.sort()
        answer.append(array2[l[2]-1])
    return answer