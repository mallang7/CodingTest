# 기능개발
import math
def solution(progresses, speeds):
    answer = []
    num = []
    for i in range(len(progresses)):
        num.append(math.ceil((100-progresses[i])/speeds[i]))
    stack=[]
    count=0
    while len(num) >0:
        if not stack:
            stack.append(num[0])
            num.pop(0)
        else:
            if num[0] <= stack[0]:
                stack.append(num[0])
                num.pop(0)
            else:
                answer.append(len(stack))
                stack=[]
                stack.append(num[0])
                num.pop(0)
        if len(num) == 0:
            answer.append(len(stack))
    return answer