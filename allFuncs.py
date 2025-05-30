def byt(n,lon=False):
    if n<0:
        return "0"*16
    s=""
    for i in range(15,-1,-1):
        if 2**i<=n:
            s+="1"
            n-=2**i
        else:
            s+="0"

    return s
def byts(byte):
    s=""
    for i in byte:
        if i=="1":s+="#"
        else:s+="_"
    return s
def num(byte):
    byte=byte[::-1]
    n=0
    for i in range(len(byte)):
        n+=int(byte[i])*2**i
    # if n!=0:
    #     print(n)
    #     input()
    return n