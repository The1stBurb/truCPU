import allVars as av
from allVars import ltrs,ltr,ltrx
from allFuncs import byt,COLOUR
from random import randint
from time import perf_counter_ns
from file_drive import files
asm=[]
"""
it no worky rn, undergoing massive renovations...
almost equivilant of tearing it all down and rebuilding...

"""
# def rect(rect_x,rect_y,rect_w,rect_h);for rect_yi rect_y <rect_h +=1;for rect_xi rect_x <rect_w +=1;pxl(rect_xi,rect_yi);frd;frd;disp();fcd 
code=""
with open("codeFiles/boot.burb")as main:
    code=main.read().replace("width",str(av.scrnWdth)).replace("height",str(av.scrnHght)).replace(";","\n")
for i in ltrx:
    code=code.replace(i,ltrx[i])
# input(code)
# input("\ksb[u"in ltrx)
# code="""
# var x=0
# x=AND(3,1)
# pxl(x,0)
# """
# Random(min,max)
# Randint(min,max)
# Round(n,mag)
# Min(n1,n2)
# Max(n1,n2)
# Dist(X1,y1,x2,y2)
# Abs(n)
# Sqrt(n)
# Fill(r,g,b) or (r,g,b,a) or (intensity) or (I,a) - done ish
# Rect(x,y,w,h)
# Ellipse(x,y,w,h)
# Line(X1,y1,X2,y2)
# Text(txt,x,y)
# Type(var)
# Istype(var,typeOfVar)
# Str(val)
# Int(val)
# List(val)
# Time()-returns time in seconds
# Millis()-returns time In milliseconds since program started
# Sleep(len)
var={"seed":[str(randint(0,255)),"int"],"COLOUR":["0","int"],"BGCOLOUR":["4095","int"]}
fnc={}
flgs={}
tk=0
lp=[]
def tok(ln):
    global tk,asm
    if ";"in ln:
        ln=ln[:ln.find(";")]
    # lne=ln[]
    # print(lne)
    asm.append(ln)
    # ln=ln.strip().split(" ")
    # print(ln,len(ln.strip().split(" ")))
    tk+=len(ln.strip().split(" "))

def args(l):
    b=l.index("(")
    l2=[l[:b],""]
    o=False
    ans=[]
    for i in l[b+1:len(l)-1]:
        if i=="," and not o:l2.append("")
        else:l2[-1]+=i
        if i=="(":
            o=True
            ans.append(len(l2)-1)
        elif i==")":o=False
    return l2,ans
def typ(l):
    return "int" if l.isdigit() else ("list" if l[0]=="[" else ("str" if l[0]=="\"" else ("bool" if l in ["false","true"] else ("dict" if l[0]=="{" else "none"))))
def fish(l):
    for i in [">=","<=","<",">","==","!="]:
        try:
            # print(l,i)
            b=l.index(i)
            l=l.split(i)
            return l[0],i,l[1]
        except:pass
    # print("why no work")
stop=False

lit={}
def lines(l,ifover=False):
    # print(type(l),l)
    if l is None:return""
    # print(l)
    global asm,tk,var,fnc,flgs,lp,stop
    if l[0]=="var":
        l=l[1].split("=")
        if "."in l[0] and l[0].split(".")[0] in lit and lit[l[0].split(".")[0]]!="":
            l[0]=l[0].split(".")
            l[0]=f"{lit[l[0][0]]}.{l[0][1]}"
        if "/"in l[0]:
            sl=[l[0].index("/"),l[0].rindex("/")]
            l[0]=[l[0][:sl[0]],l[0][sl[0]+1:sl[1]],l[0][sl[1]+1:len(l[0])-1]]
            # print(l[0])
            l[0]=f"{l[0][0]}{var[l[0][1]][0]}{l[0][2]}"
            # input(l[0])
        t=typ(l[1])
        if t=="str":
            tok(f"ldav #{len(l[1])-2}")
            # for x,i in enumerate(l[1][1:len(l[1])-1]):
            #     st=["var",f"{l[0]}[{x}]={ltr.index(i)}"]
            #     # input(st)
            #     lines(st)
            # return
        else:
            if l[1]in var:
                tok(f"lda {l[1]}")
                l[1]=var[l[1]][0]
                # print(l[1],pl)
            else:tok(f"ldav #{l[1]}")
        var[l[0]]=[l[1],t]
        tok(f"sta {l[0]}")
        # tok(f"lda")
    elif "+="in l[0]:
        l=l[0].split("+=")
        print(l)
        fm=""
        lm=""
        if "["in l[0]:
            b=l[0].index("[")
            fm=l[0][b+1:len(l[0])-1]
            l[0]=l[0][:b]
        if "["in l[1]:
            b=l[1].index("[")
            lm=l[1][b+1:len(l[1])-1]
            # print(lm,l[1],)
            l[1]=l[1][:b]
        ft=var[l[0]][1]
        if l[1]in var:lt=var[l[1]][1]
        else:lt=typ(l[1])
        print(ft,lt)
        # print(f"{l[0]}|{l[1]}|{ft}|{lt}|")
        if ft=="int":
            if lt=="int":
                # print(l,"fish")
                tok(f"lda {l[0]}")
                if l[1] in var:tok(f"ldb {l[1]}")
                else:tok(f"ldbv #{l[1]}")
                tok("add")
                tok(f"sta {l[0]}")
    elif "-="in l[0]:
        l=l[0].split("-=")
        fm=""
        lm=""
        if "["in l[0]:
            b=l[0].index("[")
            fm=l[0][b+1:len(l[0])-1]
            l[0]=l[0][:b]
        if "["in l[1]:
            b=l[1].index("[")
            lm=l[1][b+1:len(l[1])-1]
            # print(lm,l[1],)
            l[1]=l[1][:b]
        ft=var[l[0]][1]
        if l[1]in var:lt=var[l[1]][1]
        else:lt=typ(l[1])
        # print(f"{l[0]}|{l[1]}|{ft}|{lt}|")
        if ft=="int":
            if lt=="int":
                tok(f"lda {l[0]}")
                if l[1] in var:tok(f"ldb {l[1]}")
                else:tok(f"ldbv #{l[1]}")
                tok("sub")
                tok(f"sta {l[0]}")
    elif "*="in l[0]:
        l=l[0].split("*=")
        tok(f"lda {l[0]}")
    elif "="in l[0]:
        l=l[0].split("=")
        # if "."in l[0] and l[0].split(".")[0] in lit and lit[l[0].split(".")[0]]!="":
        #     l[0]=l[0].split(".")
        #     l[0]=f"{lit[l[0][0]]}.{l[0][1]}"
        # if "."in l[1] and l[1].split(".")[0] in lit and lit[l[1].split(".")[0]]!="":
        #     l[1]=l[1].split(".")
        #     l[1]=f"{lit[l[1][0]]}.{l[1][1]}"
        # if "\""in l[1]:l[1]=str(ltr.index(l[1][1]))
        # fm=""
        # lm=""
        # # if "/"in l[0]:
        # #     sl=[l[0].index("/"),l[0].index("/")]
        # #     l[0]=[l[0][:sl[0]],l[0][sl[0]+1:sl[1]],l[0][sl[1]+1:]]
        # #     input(l[0])
        # # print(l)
        # # if "["in l[1]:
        #     # par=l[1].index("[")
        #     # zd=l[1][par+1:].split(",")
        #     # st=f"{l[0]}={l[1][:par]}.__get__({zd[0]},{zd[1][:-1]})"
        #     # input(st)
        #     # lines([st])
        #     # return""
        # if "["in l[0]:
        #     b=l[0].index("[")
        #     # print(l[0],b)
        #     fm=l[0][b+1:len(l[0])-1]
        #     l[0]=l[0][:b]
        # if "["in l[1]:
        #     b=l[1].index("[")
        #     lm=l[1][b+1:len(l[1])-1]
        #     # print(lm,l[1],)
        #     l[1]=l[1][:b]
        ft=var[l[0]][1]
        if l[1]in var:lt=var[l[1]][1]
        elif "("in l[1]:lt="func"
        else:lt=typ(l[1])
        # print(ft,lt)
        if lt=="func":
            lines([l[1]])
            tok("ldav #0")
            # tok(f"sta {l[0]}")
        else:
            if l[1]in var:tok(f"lda {l[1]}")
            elif l[1][0]=="\"":tok(f"ldav #{ltr.index(l[1][1])}")
            else:tok(f"ldav #{l[1]}")
        tok(f"sta {l[0]}")
        return
        if ft=="str":
            if lt=="str":
                # print(l)
                tok(f"ldav {l[1]}")
                tok(f"ldbv #{fm}")
                # tok("incb")
                tok("add")
                # tok(f"sta #{tk+3}")
                # tok("lda #0")
                # tok(f"sta {l[0]}")
                if l[1] in var:tok(f"ldb {l[1]}")
                else:
                    # input(l[1][1:len(l[1])-1])
                    tok(f"ldbv #{l[1][1:len(l[1])-1]}")
                tok(f"sta #{tk+3}")
                tok(f"stb #0")
        if lt=="int":
            if ft=="list":
                tok(f"ldav {l[0]}")
                tok(f"ldbv #{fm}")
                tok("add")
            if l[1]in var:tok(f"ldb {l[1]}")
            else:tok(f"ldbv #{l[1]}")
            if ft=="list":
                tok(f"sta #{tk+3}")
                tok(f"stb #0")
            else:tok(f"stb {l[0]}")
        elif lt=="list":
            tok(f"ldav {l[1]}")
            tok(f"ldbv #{lm}")
            tok("add")
            tok(f"sta #"+str(tk+(3 if ft=="int" else 8)))
            if ft=="list":
                tok(f"ldav {l[0]}")
                tok(f"ldbv #{fm}")
                tok("add")
            tok("ldb #0")
            if ft=="list":
                tok(f"sta #{tk+3}")
                tok("stb #0")
            else:tok(f"stb {l[0]}")
        elif lt=="bool":
            if ft in["int","bool"]:
                if l[1]=="true":tok("ldav #1")
                else:tok("ldav #0")
                tok(f"sta {l[0]}")
        elif lt=="func":
            # print(l[1])
            lines([l[1]])
            tok("ldav #0")
            tok(f"sta {l[0]}")
    elif "("in l[0]:
        l=args(l[0])
        l=[l[0],l[1]]
        # print(l)
        if l is None:return ""
        for i in range(len(l[0])):
            if "["in l[0][i] and "]"in l[0][i]:
                print(l[0][i])
                p=[l[0][i].index("["),l[0][i].index("]")]
                if l[0][i][p[0]+1:p[1]]in var:
                    l[0][i]=l[0][i][:p[0]+1]+var[l[0][i][p[0]+1:p[1]]][0]+l[0][i][p[1]:]
                    # input(l[0][i])
            # if "."in l[0][i] and l[0][i].split(".")[0] in lit and lit[l[0][i].split(".")[0]]!="":
            #     l[0][i]=l[0][i].split(".")
            #     l[0][i]=f"{lit[l[0][i][0]]}.{l[0][i][1]}"
        if "."in l[0][0]:
            par=l[0][0].index(".")
            l[0]=[l[0][0][par+1:],l[0][0][:par]]+l[0][1:]
            # input(l[0])
        if l[0][0]in ["disp"]:
            tok("disp")
        elif l[0][0]=="AND":
            # print("anded")
            l=l[0]
            if l[1]in var:tok(f"lda {l[1]}")
            else:tok(f"ldav #{l[1]}")
            if l[2]in var:tok(f"ldb {l[2]}")
            else:tok(f"ldbv #{l[2]}")
            tok("and")
            tok(f"sta #{tk+3}")
        elif l[0][0]=="SHL":
            # print("anded")
            l=l[0]
            if l[1]in var:tok(f"lda {l[1]}")
            else:tok(f"ldav #{l[1]}")
            ln=l[2]
            if ln in var:ln=var[ln][0]
            for i in range(int(ln)):
                tok("shla")
            tok(f"sta #{tk+3}")
        elif l[0][0]=="SHR":
            # print("anded")
            l=l[0]
            if l[1]in var:tok(f"lda {l[1]}")
            else:tok(f"ldav #{l[1]}")
            ln=l[2]
            if ln in var:ln=var[ln][0]
            for i in range(int(ln)):
                tok("shra")
            tok(f"sta #{tk+3}")
        elif l[0][0]=="WRT":
            l=l[0]
            tok(f"lda {l[1]}")
            tok(f"lva")
            tok(f"lda {l[2]}")
            tok(f"lxa")
            tok(f"lda {l[3]}")
            tok("lya")
            tok("wri")
        elif l[0][0]=="char":
            l=l[0]
            b=ltr.index(l[1])
            tok(f"ldav #{b}")
            tok(f"sta #{tk+3}")
        elif l[0][0]=="pxl":
            l=l[0]
            if l[1]in var:tok(f"lda {l[1]}")
            else:tok(f"ldav #{l[1]}")
            tok("lxa")
            if l[2]in var:tok(f"lda {l[2]}")
            else:tok(f"ldav #{l[2]}")
            tok("lya")
            tok("lda COLOUR")
            tok("pxi")
        elif l[0][0]=="setFile":
            l=l[0]
            # input(f"{l[1]} , {l[1]in var}")
            if l[1] in var:
                tok(f"lda {l[1]}")
                tok(f"sta #{tk+3}")
                tok(f"stid #0")
            elif l[1][0]=="\"":tok(f"stid #{files.index(l[1][1:len(l[1])-1])}")
            else:tok(f"stid #{l[1]}")
        elif l[0][0]=="loadFile":
            pass
        elif l[0][0]=="debug":
            l=l[0]
            if len(l)>1:
                if l[1] in var:tok(f"lda {l[1]}")
                else:tok(f"ldav #{l[1]}")
            if len(l)>2 and l[2]=="0":tok("dbg1")
            else:tok("dbg")
        elif l[0][0]=="getData":
            l=l[0]
            # print("i did it")
            if l[1] in var:
                tok(f"lda {l[1]}")
                tok(f"sta #{tk+3}")
                tok(f"ldca #0")
            else:tok(f"ldca #{l[1]}")#i gotta do var thing here erg
            tok(f"sta #{tk+3}")
        elif l[0][0]=="len":
            l=l[0]
            tok(f"lda {l[1]}")
            # input(l[1])
            tok(f"sta #{tk+3}")
        elif l[0][0]=="time":
            tok(f"ldav #{round((perf_counter_ns()/10**9)*10)}")#needs to be tenths of a second
            tok(f"sta #{tk+3}")
        elif l[0][0]=="key":
            tok(f"int1 #{tk+3}")
        elif l[0][0]=="getPxl":
            l=l[0]
            if l[1] in var:
                tok(f"lda {l[1]}")
                tok(f"lxa")
            else:tok(f"lxv {l[1]}")
            if l[2] in var:
                tok(f"lda {l[2]}")
                tok(f"lya")
            else:tok(f"lyv {l[2]}")
            tok("pxg")
            tok(f"sta #{tk+3}")
        elif l[0][0]=="background":
            l=l[0]
            m=int(l[1])*256+int(l[2])*16+int(l[3])
            tok(f"ldav #{m}")
            tok("sta BGCOLOUR")
            tok("sclr")
        elif l[0][0]=="push":
            l=l[0]
            tok(f"lda {l[1]}")#get the length
            tok("inca")
            tok(f"sta {l[1]}")
            tok(f"ldbv {l[1]}")
            tok("add")
            # tok("ldbv #{ltr.index()}")
            tok(f"ldb {l[2]}")
            tok(f"sta #{tk+3}")
            tok("stb #0")
        # elif l[0][0]=="cursor":
        #     l=l[0]
        #     if l[1]=="location":
        #         tok(f"setMouseX #{l[2]}")
        #         tok(f"setMouseY #{l[3]}")
        #     elif l[1]==""
        # elif l[0][0]=="clear":

        else:
            l=l[0]
            for x,i in enumerate(l[1:]):
                f="("in i
                if "["in i:
                    b=i.index("[")
                    # print(l[0],b)
                    fm=i[b+1:len(i)-1]
                    i=i[:b]
                if f:
                    lines([i])
                    tok("ldav #0")
                elif i in var:
                    if var[i][1]=="str":
                        tok(f"ldav {i}")
                        tok(f"ldbv #{fm}")
                        tok("add")
                        tok(f"sta #{tk+3}")
                        tok("lda #0")
                    else:tok(f"lda {i}")
                elif len(i)>1 and i[0]=="\"":tok(f"ldav #{ltr.index(i[1])}")
                else:tok(f"ldav #{i}")
                f=fnc[l[0]][x]
                if f in lit:lit[f]=i
                tok(f"sta {f}")
            tok(f"call {l[0]}")
    elif l[0]=="def":
        if not stop:
            stop=True
            tok("hlt")
        l=args(l[1])[0]
        # print(l)
        for i in l[1:]:
            if i[0]=="|":
                i=i[1:len(i)-1]
                lit[i]=""
            # elif i in lit:i=
            var[i]=["0","int"]
        asm.append(f"{l[0]}:")
        # fnc[l[0]]=tk
        tok("nop")
        tok("incsp")
    elif l[0]=="fcd":
        tok("decsp")
        tok("ret")
    elif l[0]=="if":
        l=fish(l[1])
        # print(l,l is None)
        if l is None:return ""
        if "."in l[0] and l[0].split(".")[0] in lit and lit[l[0].split(".")[0]]!="":
            l[0]=l[0].split(".")
            l[0]=f"{lit[l[0][0]]}.{l[0][1]}"
        if "."in l[1] and l[1].split(".")[0] in lit and lit[l[1].split(".")[0]]!="":
            l[1]=l[1].split(".")
            l[1]=f"{lit[l[1][0]]}.{l[1][1]}"
        tok(f"lda {l[0]}")
        if l[2]in var:tok(f"ldb {l[2]}")
        else:tok(f"ldbv #{l[2]}")
        tok("cmp")
        op={"<":"jma","<=":"jma",">":"jna",">=":"jna","!=":"jme","==":"jne"}[l[1]]
        #if <= we want to do it IF a is larger OR equal - this actually works rn for <
        #if < we want to jump IF ALarger or equal, so if 
        #ALarger is 1<1, but equal is 1==1 os we need to do
        #rn jna can trigger on 1<1 os we need a !=
        tok(f"{op} "+(ifover if ifover else "ifd"))
        if l[1]in ["<",">="]:
            op={"<":"jme",">=":"jne"}[l[1]]
            tok(f"{op} "+(ifover if ifover else "ifd"))
    elif l[0]=="ifd":
        tok("ifd")
    elif l[0]=="flag":
        flgs[l[1]]=tk
        tok(f"nop")
    elif l[0]=="goto":
        tok(f"jmp {l[1]}")
    elif l[0]=="for":
        #for i 0 <3 +=1
        # print(l)
        lines(["var",f"{l[1]}={l[2]}"])
        lines([f"{l[1]}={l[2]}"])
        lp.append([tk,f"{l[1]}{l[4]}"])
        tok("nop")
        lines(["if",f"{l[1]}{l[3]}"],"frd")
    elif l[0]=="frd":
        b=lp.pop()
        lines([b[1]])
        tok(f"jmp #{b[0]}")
        tok("frd")
        # var[l[1]]=[l[2],"int"]
    elif l[0]=="while":
        lp.append([tk])
        tok("nop")
        lines(["if",l[1]],"whd")
    elif l[0]=="whd":
        b=lp.pop()
        tok(f"jmp #{b[0]}")
        tok("whd")
    elif l[0]=="return":
        tok("decsp")
        tok("popa")
        tok("ldbv #2")
        tok("add")
        if "."in l[1] and l[1].split(".")[0] in lit:
            l[1]=l[1].split(".")
            l[1]=f"{lit[l[1][0]]}.{l[1][1]}"
        if "/"in l[1]:
            sl=[l[1].index("/"),l[1].rindex("/")]
            l[1]=[l[1][:sl[0]],l[1][sl[0]+1:sl[1]],l[1][sl[1]+1:len(l[1])-1]]
            print(l[1])
            l[1]=f"{l[1][0]}{var[l[1][1]][0]}{l[1][2]}"
            input(l[1])
        if l[1]in var:tok(f"ldb {l[1]}")
        else:tok(f"ldbv #{l[1]}")
        tok(f"sta #{tk+3}")
        tok("stb #0")
        tok("ret")
        # for i in lit:
        #     lit[i]=""
c=code.split("\n")
for x in range(len(c)):
    if "#"in c[x]:
        continue
    if "displayMode"in c[x]:
        b=c[x].split("=")
        av.displayMode=b[1]
        c[x]=""
for i in c:
    if "def"in i and i[0]!="#":
        l=args(i.split(" ")[1])[0]
        fnc[l[0]]=l[1:]
for x,line in enumerate(c):
    line=line.strip()
    if "#"in line:
        line=line[:line.find("#")]
    l=line.split(" ")
    # print("|"+line+"|",len(l),l)
    if len(l)==0 or l[0]=="":
        continue
    else:lines(l)
tok("hlt")
# tok("hlt")
st=[]
lst=[]
print(var)
for i in var:
    v=var[i][1]
    p=tk
    if v=="int":
        # tok("#1;int")
        tok(f"#{var[i][0]} ;val of int from-{i}")
    elif v=="list":
        # tok(f"#2;list from {i}")
        b=var[i][0][1:len(var[i][0])-1].split(",")
        tok(f"#{len(b)} ;elements after")
        for j in b:
            # tok("#1;type")
            tok(f"#{j} ;val")
        # tok(f"loc|{i}|{len(lst)}|list")
        # lst.append(var[i][0])
    elif v=="str":
        b=list(var[i][0][1:len(var[i][0])-1])
        # tok(f"#3;this is str from {i}")
        tok(f"#{len(b)} ;elements after")
        # tok("'_")
        for j in range(10):
            if j<len(b):
                tok(f"#{ltr.index(b[j])} ;val of ltr")
            else:
                tok("#0 ; val of ltr extnd")
    elif v=="bool":
        if var[i][0]=="false":
            tok("#5 ;bool-false")
        elif var[i][0]=="true":
            tok("#4 ;bool-true")
    elif v=="none":
        tok("#8 ;null")
    # asm.append(f"#{var[i]}")
    var[i]=p
    # print(p,i)
tk=0
# print(asembly)
for x,line in enumerate(asm):
    if ";"in line:
        line=line[:line.find(";")]
    l=line.strip().split(" ")
    # print(l)
    if ":"in l[0]:
        continue
    tk+=len(l)
    # elif len(l)
    if l[0]=="ifd":
        asm[x]="nop"
        px=0
        for i in range(x-1,-1,-1):
            if "ifd"in asm[i]:
                b=asm[i].split(" ")
                asm[i]=b[0]+f" #{tk-1}"
                print("    ",asm[i])
                px=i
            if px-1==i:
                break
    elif l[0]=="frd":
        asm[x]="nop"
        px=0
        for i in range(x-1,-1,-1):
            if "frd"in asm[i]:
                b=asm[i].split(" ")
                asm[i]=b[0]+f" #{tk-1}"
                print("    ",asm[i])
                px=i
            if px-1==i:
                break
    elif l[0]=="whd":
        asm[x]="nop"
        px=0
        for i in range(x-1,-1,-1):
            if "whd"in asm[i]:
                b=asm[i].split(" ")
                asm[i]=b[0]+f" #{tk-1}"
                print("    ",asm[i])
                px=i
            if px-1==i:
                break
    elif l[0]=="jmp"and l[1] in flgs:
        asm[x]=f"jmp #{flgs[l[1]]}"
    for i in var:
        l=asm[x].split(" ")
        if i in l:
            b=l.index(i)
            # print(i,l,var[i])
            asm[x]=" ".join(l[:b]+["#"+(str(var[i]))]+l[b+1:])
    print(asm[x]+"|",tk-1)
asembly="\n".join([i for i in asm if i!=""])+"""

"""#+"\nhlt"
# print("\n"+asembly)
# print(asembly)