import allVars as av
from allFuncs import byt,COLOUR
from random import randint
asm=[]
"""
it no worky rn, undergoing massive renovations...
almost equivilant of tearing it all down and rebuilding...

"""
#var b=[1,2,3]
#var c="abc123"
# var d=true
# var e=null
# def add adda addb\nadda+=addb\nreturn adda\nfcd
# def sub suba subb\nsuba-=subb\nreturn suba\nfcd
#
# def rect(rect_x,rect_y,rect_w,rect_h);for rect_yi rect_y <rect_h +=1;for rect_xi rect_x <rect_w +=1;pxl(rect_xi,rect_yi);frd;frd;disp();fcd 
code="""
displayMode=manual
var x=1
# x=dist(0,9,0,2)
fill(0,15,15)
pxl(x,0)
# disp()
ellipse(6,5,4)
def randint(randint_min,randint_max)
    seed=mult(74624,seed)
    seed=add(seed, 6358)
    var randint_temp=0
    randint_temp=sqr(2,16)
    seed=mod(seed,randint_temp)
    return seed
fcd
def mod(mod_a,mod_b)
    var mod_temp=0
    mod_temp=div(mod_a,mod_b)
    mod_temp=mult(mod_b,mod_temp)
    mod_temp=sub(mod_a,mod_temp)
    return mod_temp
fcd
def mult(mult_a,mult_b)
    # mult_a*=mult_b
    # return mult_b
    # pxl(mult_a,mult_b)
    var mult_x=0
    var mult_a1=0
    var mult_b1=0
    if mult_a>mult_b
        mult_a1=mult_a
        mult_b1=mult_b
    ifd
    if mult_b>mult_a
        mult_a1=mult_b
        mult_b1=mult_a
    ifd
    for mult_i 0 <mult_b1 +=1
        # shl(mult_x)
        mult_x+=mult_a1
    frd
    # # pxl(mult_x,2)
    return mult_x
fcd
def add(add_a,add_b)
    add_a+=add_b
    return add_a
fcd
def div(div_a,div_b)
    var div_t=0
    while div_a>div_b
        div_a-=div_b
        div_t+=1
    whd
    # pxl(div_t,3)
    return div_t
fcd
def sub(sub_a,sub_b)
    sub_a-=sub_b
    return sub_a
fcd
def sqr(sqr_a,sqr_b)
    var sqr_x=sqr_a
    for i 1 <sqr_b +=1
        sqr_a=mult(sqr_a,sqr_x)
    frd
    pxl(sqr_a,4)
    return sqr_a
fcd
def sub2(sub2_a,sub2_b)
    if sub2_a>sub2_b
        sub2_a-=sub2_b
        return sub2_a
    ifd
    sub2_b-=sub2_a
    return sub2_b
fcd
def root(root_num,root_factor)
    var root_guess=0
    var root_guessPow=0
    root_guess=div(root_num,2)
    root_guessPow=sqr(root_guess,2)
    while root_guessPow>root_num
        root_guess-=1
        root_guessPow=sqr(root_guess,2)
        pxl(root_guess,2)
    whd
    return root_guess
fcd
def dist(dist_x1,dist_y1,dist_x2,dist_y2)
    dist_x1=sqr(sub2(dist_x1,dist_x2),2)
    dist_y1=sqr(sub2(dist_y1,dist_y2),2)
    # dist_x2=sqr(dist_x2,2)
    var dist_add=0
    dist_add=add(dist_x1,dist_y1)
    dist_add=root(dist_add,2)
    return dist_add
fcd
# def dist2(dist2_1,dist2_2)
#     var dist2_add=0
#     dist2_add=sub2(dist2_1,dist2_2)
#     return dist2_add
# fcd
def fill(fill_red,fill_green,fill_blue) 
    var fill_temp=0
    # fill_red=div(fill_red,17)
    # fill_green=div(fill_green,17)
    # fill_blue=div(fill_green,17)
    COLOUR=fill_blue
    fill_temp=mult(fill_green,16)
    COLOUR=add(COLOUR,fill_temp)
    fill_temp=mult(fill_red,256)
    # fill_temp=mult(fill_temp,16)
    COLOUR=add(COLOUR,fill_temp)
fcd
def ellipse(ellipse_x,ellipse_y,ellipse_r)
    var ellipse_d=0
    # ellipse_r=div(ellipse_r,2)
    # pxl(ellipse_r,0)
    # pxl(ellipse_x,8)
    # pxl(ellipse_y,9)
    var ellipse_x2=ellipse_x
    ellipse_x2+=ellipse_r#add(ellipse_x,ellipse_r)
    var ellipse_y2=0
    ellipse_y2=add(ellipse_y,ellipse_r)
    # pxl(ellipse_x2,12)
    # pxl(ellipse_y2,13)
    var ellipse_cx=ellipse_x
    var ellipse_cy=ellipse_y
    ellipse_x-=ellipse_r
    ellipse_y-=ellipse_r
    # pxl(ellipse_x,10)
    # pxl(ellipse_y,11)
    for ellipse_iy ellipse_y <=ellipse_y2 +=1
        for ellipse_ix ellipse_x <=ellipse_x2 +=1
            var ellipse_dist=0
            # ellipse_dist=dist(ellipse_cx,ellipse_cy,ellipse_iy,ellipse_ix)
            if ellipse_dist<ellipse_r
                pxl(ellipse_ix,ellipse_iy)
            ifd
        frd
        # disp()
    frd
    disp()
fcd
""".replace("width",str(av.scrnWdth)).replace("height",str(av.scrnHght)).replace(";","\n")
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
var={"seed":[str(randint(0,255)),"int"],"COLOUR":["4095","int"]}
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
def lines(l,ifover=False):
    # print(l)
    global asm,tk,var,fnc,flgs,lp,stop
    if l[0]=="var":
        l=l[1].split("=")
        if l[1]in var:
            tok(f"lda {l[1]}")
            l[1]=var[l[1]][0]
            # print(l[1],pl)
        else:tok(f"ldav #{l[1]}")
        var[l[0]]=[l[1],typ(l[1])]
        tok(f"sta {l[0]}")
        # tok(f"lda")
    elif "+="in l[0]:
        l=l[0].split("+=")
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
        elif "("in l[1]:lt="func"
        else:lt=typ(l[1])
        if ft=="str":
            if lt=="str":
                tok(f"ldav {l[0]}")
                tok(f"ldbv #{fm}")
                tok("add")
                if l[1]in var:tok(f"ldb {l[1]}")
                else:tok(f"ldbv '{l[1][1:len(l[1])-1]}")
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
        print(l)
        if l[0][0]in ["disp"]:
            tok("disp")
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
        else:
            l=l[0]
            for x,i in enumerate(l[1:]):
                f="("in i
                if f:
                    lines([i])
                    tok("ldav #0")
                elif i in var:tok(f"lda {i}")
                else:tok(f"ldav #{i}")
                tok(f"sta {fnc[l[0]][x]}")
            tok(f"call {l[0]}")
    elif l[0]=="def":
        if not stop:
            stop=True
            tok("hlt")
        l=args(l[1])[0]
        print(l)
        for i in l[1:]:
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
        print(l)
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
        print(l)
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
        if l[1]in var:tok(f"ldb {l[1]}")
        else:tok(f"ldbv #{l[1]}")
        tok(f"sta #{tk+3}")
        tok("stb #0")
        tok("ret")
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
                tok(f"'{b[j]} ;val of ltr")
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