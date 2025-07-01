# print(type(eval("1+2")))

quit()

ops={
    "nop":"0000_0000",
    "lda":"0000_0010","ldb":"0000_0011","sta":"0000_0100","stb":"0000_0101","ldac":"0000_0110","ldbc":"0000_0111","stac":"0000_1000","stbc":"0000_1001","nota":"0000_1010","notb":"0000_1011","shlb":"0000_1101","shla":"0000_1100","shrb":"0000_1111","shra":"0000_1110","incb":"0001_0001","inca":"0001_0000","decb":"0001_0011","deca":"0001_0010","popb":"0001_0101","popa":"0001_0100","psha":"0001_0110","pshb":"0001_0111","add":"0001_1000","sub":"0001_1001","and":"0001_1010","or":"0001_1011","xor":"0001_1100","cmp":"0001_1101","swap":"0001_1110",
    "jmp":"0011_0000","jmz":"0011_0010","jnz":"0011_0011","jmc":"0011_0100","jnc":"0011_0101",
    "incsp":"0010_0000","decsp":"0010_0001","push":"0010_0010","pop":"0010_0011",
    
    "pxi":"0100_0000","pxo":"0100_0001","lpxa":"0100_0010","lpxb":"0100_0011","spxa":"0100_0100","spxb":"0100_0101","wrt":"0100_0110",
    "hlt":"1000_0000",
}
# op={ops[i]:i for i in ops}
#ram.mem[ad].e=0011_0xxx,s4 or 0100_0xxx,s4 or 0000_0xxx,s4 or 0000_001x,s5 and not 0000_011x
#mar.s=0000_0xxx,s4 or 0100_0xxxx,s6 or 0011_0xxx,s6 and not 0000_011x
#iar.e=0100_0xxx,s5 or 0011_0xxx,s5 or 0000_0xxx,s6 and not 0000_011x
#iar.s=0100_0xxx,s6 or 0011_0xxx,s6 or 0000_0xxx,s7 and not 0000_011x
#ram.s=0000_010x,s5
#a.e=0000_1xx0,s4 or 0001_0xx0,s4 or 0000_0100,s5 or 0100_0100,s7 and not 0000_1000 or 0001_0100
#a.s=0000_0010,s5 or 0000_1xx0,s5 or 0001_00x0,s5
#b.e=0000_1xx1,s4 or 0001_0xx1,s4 or 0000_0101,s5 or 0100_0101,s7 and not 0000_1001 or 0001_0101
#b.s=0000_0011,s5 or 0000_1xx1,s5 or 0001_00x1,s5
#sp.e=0010_000x,4
#sp.s=0010_000x,s5
#acc.s=0000_1xxx,s4 or 0001_00xx,s4 or 0010_000x,s4 or 0100_0xxx,s5 or 0011_0xxx,s5 or 0000_0xxx,s6 and not 0000_011x or 000_100x
#acc.e=0000_1xxx,s5 or 0001_00xx,s5 or 0010_000x,s5 or 0000_0xxx,s7 and not 0000_011x or 0000_100x
#stk.s=0001_011x,s4
#stk.e=(0001_010x,s4
#gpu.s=[0100_0xxx,s4 or s7

def cm(a,b):
    a=a.replace("_","")
    b=b.replace("_","")
    for i in range(len(a)):
        if a[i]=="x" or b[i]=="x":
            continue
        if a[i]!=b[i]:
            return False
    return True
def tst(a):
    # print(a)
    if (cm(a,"0000_0xxx")or cm(a,"0100_0xxx")or cm(a,"0011_0xxx")) and not cm(a,"0000_011x"):
        return True
    return False

for i in ops:
    if tst(ops[i]):
        print(i)