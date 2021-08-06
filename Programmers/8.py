# 문자열 압축
def solution(s):
    length=[]
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2 +1):
        result = ""
        count = 1
        tempStr = s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i] == tempStr:
                count +=1
            else:
                if count ==1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[j:j+i]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
    return min(length)