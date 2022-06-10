# lev.2 피로도
from itertools import permutations
def solution(k, dungeons):
    answer = []
    dungeon = list(permutations(dungeons))
    for d in dungeon:
        k2 = k
        ans=0
        for i in d:
            if k2 >= i[0]:
                k2 -= i[1]
                ans += 1
        answer.append(ans)
        
    return max(answer)