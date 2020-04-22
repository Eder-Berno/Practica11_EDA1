def fibonacci_iterativo_vl(numero):
    f1=0
    f2=1
    tmp=0
    for i in range(1,numero-1):
        tmp = f1+f2
        f1 = f2
        f2 = tmp
    return f2
        
