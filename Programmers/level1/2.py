# 렙1 - 키패드 누르기
def solution(numbers, hand):
    numbers = [str(i) for i in numbers]
    answer = ''
    num = {'1':(-1,3),'4':(-1,2),'7':(-1,1),'*':(-1,0),
           '3':(1,3),'6':(1,2),'9':(1,1),'#':(1,0),
           '2':(0,3),'5':(0,2),'8':(0,1),'0':(0,0)}
    prev_left = '*'
    prev_right = '#'
    for i in numbers:
        if num[i][0] == -1:
            answer += 'L'
            prev_left = i
        elif num[i][0] == 1:
            answer += 'R'
            prev_right = i
        else:
            left_distance = abs(num[prev_left][0]-num[i][0]) + abs(num[prev_left][1]-num[i][1])
            right_distance = abs(num[prev_right][0]-num[i][0]) + abs(num[prev_right][1]-num[i][1])
            if left_distance < right_distance:
                answer += 'L'
                prev_left = i
            elif left_distance > right_distance:
                answer += 'R'
                prev_right = i
            else: #거리가 같을때
                if hand == 'left':
                    answer += 'L'
                    prev_left = i
                else:
                    answer += 'R'
                    prev_right = i
    return answer