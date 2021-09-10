# 가장 큰 수
import itertools
def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num*3, reverse = True)
    answer = str(int(''.join(numbers_str)))
    return answer