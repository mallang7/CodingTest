# 3. 문자열 뒤집기 (313p)

S = list(map(int,input()))

result = 0
count_0 = []
count_1 = []
count0 = 1
count1 = 1

prior = S[0]
for i in range(1,len(S)):
    if S[i] == prior:
        if S[i]==0:
            count0 += 1
        else:
            count1 += 1
        prior = S[i]
    else:
        if prior ==0:
            count_0.append(count0)
        else:
            count_1.append(count1)
        count0 = 1
        count1 = 1
        prior = S[i]

if S[-1] == 0:
    count_0.append(count0)
else:
    count_1.append(count1)


result = min(len(count_0),len(count_1))
print(count_0,count_1)
print(result)