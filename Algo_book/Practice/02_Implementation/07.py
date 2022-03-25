# 07. 럭키 스트레이트
def solution(N):
    N_str = str(N)
    left = N_str[:len(N_str)//2]
    right = N_str[len(N_str)//2:]
    if sum(left) == sum(right):
        return "LUCKY"
    return "READY"

print(solution(123402))
print(solution(7755))