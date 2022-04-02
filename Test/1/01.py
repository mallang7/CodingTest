#동전

money1 = 4578
costs1 = [1,4,99,35,50,1000]

money2 = 1999
costs2 = [2,11,20,100,200,600]

def solution(money,costs):
    result = 0
    coin = [1,5,10,50,100,500]
    used = [0] *6
    mon = money
    while mon != 0:
        count = []
        price=[]
        for i in range(6):
            count.append(mon//coin[i])
            price.append(costs[i]*count[i])
        min_money = min(price)
        min_index = price.index(min_money)
        used[min_index] += count[min_index]
        mon -= count[min_index]*coin[min_index]
        result += min_money
    return result

print(solution(money1,costs1))
print(solution(money2,costs2))