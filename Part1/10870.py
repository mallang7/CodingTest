# 10870 - 피보나치 5
N = int(input())
fib=[]
fib.append(0)
fib.append(1)
for i in range(2,N+1):
    fib.append(fib[i-1] + fib[i-2])
    
print(fib[N])
    