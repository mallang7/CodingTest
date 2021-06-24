#10162번 전자레인지

T = int(input())
if (T % 10) != 0:
    print("-1")
else:
    A = 300
    B = 60
    C = 10
    a=b=c= 0
    a = T//A
    T = T - A*a
    b = T//B
    T = T - B*b
    c = T//C
    print(a, b, c)