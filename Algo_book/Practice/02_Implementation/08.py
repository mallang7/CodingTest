# 문자열 재정렬

from string import ascii_uppercase
def solution(S):
    S_list = list(S)
    alphabet_list = list(ascii_uppercase)
    alphabet =[]
    number = []
    for s in S_list:
        if s in alphabet_list:
            alphabet.append(s)
        else:
            number.append(int(s))
    alphabet.sort()
    return "".join(alphabet)+str(sum(number))

print(solution('K1KA5CB7'))