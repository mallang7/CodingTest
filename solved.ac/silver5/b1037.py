N = int(input())
number = list(map(int,input().split()))
def solution(num):
    answer = 1
    num.sort()
    if len(num) == 1:
        answer = num[0]*num[0]
    elif len(num) % 2 == 1:
        answer = (num[len(num)//2])*(num[len(num)//2])
    else:
        answer = num[0]*num[-1]
    return answer
ans = solution(number)
print(ans)
