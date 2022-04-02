# 레벨1 - 3진법 뒤집기
def solution(n):
    answer = 0
    three_rev = []
    a = 0 #몫
    b = 0 #나머지
    if n == 1:
        return 1
    while (n // 3) != 0:
        a = n // 3
        b = n % 3
        three_rev.append(b)
        n = n // 3
    three_rev.append(a)
    three_rev.reverse()
    for i in range(len(three_rev)):
            answer += pow(3,i) * three_rev[i]
        
    return answer