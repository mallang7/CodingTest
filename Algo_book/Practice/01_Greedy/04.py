from itertools import combinations
N = int(input())
coins=list(map(int,input().split()))

coins.sort()
money=coins.copy()
for i in range(2,len(coins)):
    money+=list(combinations(coins,i))
print(money)

sum_li=[]
for i in range(len(money)):
    sum_li.append(sum(money[i]))

print(sum_li)
    
    
count = 0  
while True:
    count += 1
    for i in money:
        if count == sum(i):
            continue
        else:
            break

print(count)