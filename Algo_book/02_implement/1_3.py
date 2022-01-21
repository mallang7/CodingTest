# 구현 - 왕실의 나이트 115p
A = input()
x=ord('a')-ord(A[0])+1
y=int(A[1])

datas=[(-2,-1),(-2,1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]
count=0
for data in datas:
    next_row= x + data[0]
    next_column= y + data[1]
    if (next_row >=1 and next_row <=8) and (next_column >=1 and next_column <=8):
        count += 1
print(count)
