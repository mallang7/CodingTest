import sys
input=sys.stdin.readline
def check_bw(matrix):
    case1_not_match = 0
    case2_not_match = 0

	# case 1 시작점(0,0)이 W 인경우 
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "W":
                    case1_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "B":
                    case1_not_match += 1
	
    # case 2 시작점(0,0)이 B 인경우 
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 == 1) and (y % 2 == 1)):  # 행짝 열짝, 행홀 열홀
                if matrix[x][y] != "B":
                    case2_not_match += 1

            elif ((x % 2 == 1) and (y % 2 == 0) or (x % 2 == 0) and (y % 2 == 1)):  # 행홀 열짝, 행짝 열홀
                if matrix[x][y] != "W":
                    case2_not_match += 1

    return min(case1_not_match, case2_not_match)
        
def solution():
    input_list=[]
    min_revise_cnt = 123041234723842
    M, N = map(int,input().split())
    for i in range(M):
        input_list.append(input())
    for row in range(M-7):
        for col in range(N-7):
            slice_mat = [one_row[col:col+8] for one_row in input_list[row:row+8]]
            revise_cnt = check_bw(slice_mat)
            min_revise_cnt = min(min_revise_cnt,revise_cnt)
    return min_revise_cnt
print(solution())
