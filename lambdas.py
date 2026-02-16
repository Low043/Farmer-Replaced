def lambda1(fn, arg1):
    def lamb():
        fn(arg1)
    return lamb

def lambda2(fn, arg1, arg2):
    def lamb():
        fn(arg1, arg2)
    return lamb

def lambda3(fn, arg1, arg2, arg3):
    def lamb():
        fn(arg1, arg2, arg3)
    return lamb
    
def lambda4(fn, arg1, arg2, arg3, arg4):
    def lamb():
        fn(arg1, arg2, arg3, arg4)
    return lamb
    
def lambda5(fn, arg1, arg2, arg3, arg4, arg5):
    def lamb():
        fn(arg1, arg2, arg3, arg4, arg5)
    return lamb
    
def lambda6(fn, arg1, arg2, arg3, arg4, arg5, arg6):
    def lamb():
        fn(arg1, arg2, arg3, arg4, arg5, arg6)
    return lamb
    
def loop_lambda(fn):
    def lamb():
        while True:
            fn()
    return lamb
