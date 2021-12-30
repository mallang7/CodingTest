X = int(input())
num = [64,32,16,8,4,2,1]
count = 0
for i in num:
    if X >= i:
        X -= i
        count += 1
print(count)
