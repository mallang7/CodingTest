# # 06. 무지의 먹방 라이브 (316p)

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1
    q= []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    sum_value = 0
    previous =0
    
    length = len(food_times)
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value) % length][1]


# def turn(index,idx):
#     if index == len(idx)-1:
#         index = 0
#     else:
#         index += 1
#     return index
        
# def solution(food_times,k):
#     idx = [i for i in range(len(food_times))]
#     index = idx[0]
    
#     while (k != 0):
#         if food_times[index] == 0:
#             idx.remove(index)
#             index = turn(index,idx)
#         else:
#             food_times[index] -= 1
#             index = turn(index,idx)
#         if (k ==0):
#             index = turn(index,idx)
#         if (len(idx)==0):
#             index = -1
#             break
#         k -= 1
#     return index