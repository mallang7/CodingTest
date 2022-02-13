from itertools import permutations


from itertools import combinations
N = int(input())
coins=list(map(int,input().split()))

coins.sort()
money=[]
for i in range(1,len(coins)):
    money+=(list(combinations(coins,i)))
count = 0
while True:
    count += 1
    for i in money:
        if count == sum(i):
            continue
        else:
            break

print(count)