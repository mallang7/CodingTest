# 02. 곱하기 혹은 더하기 (312p)
S = input()
s_list=[]
for i in range(len(S)):
    s_list.append(int(S[i]))

result=0
for i in s_list:
    if i == 0 or i == 1 or result==0 :
        result += i
    else:
        result *= i
        
print(result)