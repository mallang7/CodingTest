# 멀쩡한 사각형
import math
def solution(w,h):
    answer = 1
    g = math.gcd(w,h)
    answer = w*h - (w+h-g)
    return answer