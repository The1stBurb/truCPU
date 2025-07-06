from allFuncs import byt,bin_hex,bitSize
from allVars import ltrs,ltr,ltrx
from math import ceil
fnt=""
the_font="4x6"
with open(f"FONTS/{the_font}.txt","r")as f:
    fnt=f.read()#.split(">>")
for i in ltrx:
    fnt=fnt.replace(i,ltrx[i])
fnt=fnt.split(">>")
wd,hg=int(fnt[0][0]),int(fnt[0][2])
# bitSz=ceil(wd+hg)
def late(v):
    return "1"if v=="#"else "0"
def parseData(val,dat,bl=bitSize):
    dat=dat.split("\n")
    for i in range(len(dat)):
        dat[i]=dat[i].split("|")
    ltrs={}
    j=0
    for i in range(len(dat[0])-1):
        v=val[i]
        ltrs[v]=[]
        for j in range(len(dat)-1):
            ltrs[v].append("".join([late(k) for k in dat[j][i]]))
        nw=[""]
        cl=0
        for j in ltrs[v]:
            if cl+len(j)<=bl:
                cl+=len(j)
                nw[-1]+=j
            else:
                cl=0
                nw.append(j)
        ltrs[v]=nw
    return ltrs
fnts={}
for i in range(1,len(fnt),2):
    fnts=fnts|parseData(fnt[i],fnt[i+1][1:])
# print(fnts["a"],fnts["c"])
bad=[]
for i in ltr:
    if not (i in fnts):bad.append(i)
if len(bad)>0:
    print(f"ERROR: font \"{the_font}\" didn't parse the characters: {",".join([i for i in bad])}!")
    quit()
with open(f"codeFiles/{the_font}.fnt","w")as f:
    st=bin_hex(byt(wd))+bin_hex(byt(hg))+bin_hex(byt(ceil((wd*hg)/bitSize)))
    for i in fnts:
        # st+=bin_hex(byt(ltrs[i]))
        for j in fnts[i]:
            # print(j)
            st+=bin_hex(j)
    f.write(st)#"".join([f"{byt(ltrs[i])}{"".join([j for j in fnst[i]])}" for i in fnts]))