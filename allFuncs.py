bitSize=16

def byt(n,lon=False):
    if n<0:
        return "0"*bitSize
    s=""
    for i in range(bitSize-1,-1,-1):
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
def COLOUR(r,g,b):
    return r*256+g*16+b
def bin_hex(bin_str):
    if len(bin_str)<bitSize:bin_str=bin_str+("0"*(bitSize-len(bin_str)))
    if len(bin_str) != bitSize or any(c not in '01' for c in bin_str):
        raise ValueError("Input must be a 16-character string of '0's and '1's.")
    return hex(int(bin_str, 2))[2:].zfill(4)
def hex_bin(hex_str):
    if len(hex_str) != 4 or any(c not in '0123456789abcdefABCDEF' for c in hex_str):
        raise ValueError("Input must be a 4-character hexadecimal string.")
    return bin(int(hex_str, 16))[2:].zfill(16)
print(num(hex_bin("0038"))/17,num(hex_bin("0044"))/17,num(hex_bin("00E8"))/17)