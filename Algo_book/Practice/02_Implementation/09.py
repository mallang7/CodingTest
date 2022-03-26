# 문자열 압축
def solution(s):
    length =[]
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2 +1):
        temp_str = s[:i]
        a = ''
        count = 1
        for j in range(i,len(s),i):
            if s[j:i+j] == temp_str:
                count += 1
            else:
                if count == 1:
                    count =""
                a += str(count) + temp_str
                temp_str = s[j:j+i]
                count = 1
        if count ==1:
            count = ""
        a += str(count) + temp_str    
        length.append(len(a))
            
    return min(length)