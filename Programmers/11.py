# 소수찾기
import itertools
import math

def is_prime(n):
    if n<2: return False
    to = int(math.sqrt(n))+1
    for i in range(2, to):
        if n % i ==0: return False
    return True

def solution(number):
    answer = 0
    candidate = set()
    for i in range(len(number)):
        numbers = set(map(int,map(''.join, itertools.permutations(number, i+1))))
        candidate = candidate | numbers
        
    candidate = list(candidate)
    for n in candidate:
        if is_prime(n):
            answer +=1
    return answer