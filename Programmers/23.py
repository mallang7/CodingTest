#주식 가격
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        answer[i] = len(prices) - i - 1
        for j in range(i+1,len(prices)):
            if prices[j] < prices[i]:
                answer[i] -= (len(prices)-j-1)
                break
                
    return answer