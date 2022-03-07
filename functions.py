#math functions for calculator

def parse(s):
    arg1 = 0
    arg2 = 0
    op = ""
    flag = 0
    for c in s:
        if flag == 0:
            if c in '1234567890':
                arg1 += c
            else:
                op = str(c)
                flag = 1
        elif flag != 0:
            if c in '1234567890':
                arg2 += c
    #run correct operation based on 'op' command
    ret = compute(op, arg1, arg2)
    return ret

        
def compute(operator, a, b):
    match operator:
        case '+':
            return fadd(a,b)
        case '-':
            return fsubtract(a,b)
        case '/':
            return fdiv(a,b)
        case 'x':
            return fmult(a,b)

def fadd(a, b):
    ret = a + b
    return ret

def fsubtract(a, b):
    ret = a - b
    return ret

def fmult(a, b):
    ret = a * b
    return ret

def fdiv(a,b):
    ret = a/b
    return ret
