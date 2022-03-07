#math functions for calculator

def parse(s):
    #arg and op strings to represent the numbers in calculation
    arg1 = ""
    arg2 = ""
    op = ""
    flag = 0    #flag used to separate arg1 and arg2
    for c in s:
        if flag == 0:
            if c in '1234567890':
                arg1 += c
            else:
                op = c
                flag = 1
        else:
            if c in '1234567890':
                arg2 += c
    #run correct operation based on 'op' command
    ret = compute(op, int(arg1), int(arg2))
    return ret

        
def compute(operator, a, b):
    #switch statement to determine which operation function to run
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
