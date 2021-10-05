# 카카오 인턴 - 수식최대화
from itertools import permutations
from collections import deque
def solution(expression):
    answer=0
    ops=["*","+","-"]
    li=[]
    s=0
    for i, v in enumerate(expression):
        if v in ["*","+","-"]:
            li.append(expression[s:i])
            li.append(v)
            s=i+1
    else:
        li.append(expression[s:])
    for op in ops:
        if op not in expression:
            ops.remove(op)
    priority=permutations(ops)
    
    for case in priority:
        stacks = [deque(li),deque()]
        t1=1
        for c in case:
            t1=(t1+1) % 2
            t2=(t1+1) % 2
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                if len(stacks[t2])!=0 and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n=stacks[t2].pop()
                    item = str(eval(str(n)+c+str(item)))
                stacks[t2].append(item)
        result=stacks[len(ops)%2].pop()
        result = abs(int(result))
        answer = max(answer,result)
    return answer

# 참고 - https://latte-is-horse.tistory.com/132
# String을 enumerate하면 한글자씩
# eval은 string 수식을 넣어주면 파이썬 코드로 돌려서 연산해줌
# stack안에서 토글하는 법