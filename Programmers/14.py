# 2020 카카오 - 괄호변환
def solution(p):
    p=list(p)
    def split(lst):
        # u=[]
        # v=[]
        # index=0
        # for i in range(len(lst)):
        #     if u.count('(') == u.count(')'):
        #         index = i
        #         break
        #     else:
        #         u.append(lst[i])
        
        left_cnt = 0
        right_cnt = 0
        cut_idx = 0
        for i in range(len(lst)):
            if lst[i] == '(':
                left_cnt += 1
            elif lst[i] == ')':
                right_cnt += 1
            if left_cnt == right_cnt:
                cut_idx = i
                break
        u, v = lst[0:i+1], lst[i+1:]
        return (u,v)

    def is_right(u_lst):
        lst = u_lst
        stack = []
        idx = 0
        while idx < len(lst):
            first_idx = lst[idx]
            if not stack:
                stack.append(first_idx)
            elif stack[-1] == '(' and first_idx == ')':
                stack.pop(-1)
            else:
                stack.append(first_idx)
            idx += 1
        if stack:
            return False
        else:
            return True

    def convert(u):
        u=u[1:-1]
        if len(u)==0:
            return []
        else:
            for i in range(len(u)):
                if u[i]=='(':
                    u[i]=')'
                else:
                    u[i]='('
        return u
    
    def change(w):
        if len(w)==0:
            return []
        u,v=split(w)
        if is_right(u):
            return u + change(v)
        else:
            new_u = convert(u)
            return ['('] + change(v)+ [')'] +new_u
    return (''.join(change(p)))