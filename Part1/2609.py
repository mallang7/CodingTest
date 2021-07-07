# 2609 - 최대공약수와 최소공배수
n, m = map(int,input().split())
g=1
l=1
great=[]
for i in range(1,min(n,m)+1):
    if n%i==0 and m%i==0:
        great.append(i)
g=max(great)
l=n*m//g

print(g)
print(l)