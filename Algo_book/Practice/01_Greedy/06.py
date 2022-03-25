# 06. 무지의 먹방 라이브 (316p)
def turn(index,idx):
    if index == len(idx)-1:
        index = 0
    else:
        index += 1
    return index
        
def solution(food_times,k):
    idx = [i for i in range(len(food_times))]
    index = idx[0]
    
    while (k != 0):
        if food_times[index] == 0:
            idx.remove(index)
            index = turn(index,idx)
        else:
            food_times[index] -= 1
            index = turn(index,idx)
        k -= 1
        if (k ==0):
            index = turn(index,idx)
    return index