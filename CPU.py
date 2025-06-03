from register import REG
from time import sleep
from allVars import rect,bitSize,font,screen
from allFuncs import byts,num,byt
import pygame
from ALU import ALU

# from CLK import CLK
def XOR(b1,b2):
    b1,b2=int(b1),int(b2)
    return str(int(b1!=b2))
def nt(n):
    return int(not int(n))

ltrs={
    "A":33,"B":34,"C":35,"D":36,"E":37,"F":38,"G":39,"H":40,"I":41,"J":42,"K":43,"L":44,"M":45,"N":46,"O":47,"P":48,"Q":49,"R":50,"S":51,"T":52,"U":53,"V":54,"W":55,"X":56,"Y":57,"Z":58,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"1":64,"2":65,"3":66,"4":67,"5":68,"6":69,"7":70,"8":71,"9":72,"0":73,"~":74,"!":75,"@":76,"#":77,"$":78,"%":79,"^":80,"&":81,"*":82,"(":83,")":84,"_":85,"-":86,"+":87,"=":88,"{":89,"[":90,"}":91,"]":92,"|":93,"\\":94,":":95,";":96,"\"":97,"'":98,"<":99,",":100,">":101,".":102,"?":103,"/":104," ":105,"☒":0,#"¯":105,
    "\x1b[D":128,#lft
    "\x1b[A":129,#up
    "\x1b[C":130,#rght
    "\x1b[B":131,#dwn
    "\x01":132,#bckspace aka ctrl-a
}
ktb={i:byt(ltrs[i]) for i in ltrs}
def cm(a,b):
    a=a.replace("_","")
    b=b.replace("_","")
    for i in range(len(a)):
        if a[i]=="x" or b[i]=="x":
            continue
        if a[i]!=b[i]:
            return False
    return True
psz=3
def registerDisp(x,y,data,name):
    rect(x-1,y-1,bitSize*psz+2,psz+2,(0,0,0))
    for xo,i in enumerate(data):
        rect(x+xo*psz,y,psz,psz,(0,0,0) if i=="0" else (255,255,255))
    screen.blit(font.render("REG: "+name, True, (0, 0, 0)), (x, y+psz+2))

ula=ALU()
class CPU:
    def __init__(self):
        self.a=REG()
        self.b=REG()
        self.x=REG()
        self.y=REG()
        self.v=REG()
        self.sp=REG()
        self.marx=REG()
        self.mary=REG()
        self.ir=REG()
        self.iar=REG()
        self.acc=REG()
        self.bus=REG(always_set=True)
        self.tmp=REG()
        self.sp=REG()
        self.gpu=REG()
        self.int=REG()
        self.fc,self.fa,self.fz,self.fe="0","0","0","0"
        # self.hlt="10000000"
        self.aluop="00011xxx"
        self.nop=0
        self.lda,self.ldb,self.ldav,self.ldbv,self.sta,self.stb,self.lxa,self.lxb,self.lya,self.lyb,self.lva,self.lvb,self.lxv,self.lyv,self.lvv=2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        self.nota,self.notb,self.shla,self.shlb,self.shra,self.shrb,self.inca,self.incb,self.deca,self.decb,self.add,self.sub,self.ro,self.xor,self.psha,self.pshb,self.popa,self.popb,self.lpxa,self.lpxb,self.spxa,self.spxb,self.incsp,self.decsp,self.call,self.ret,self.cpm,self.nad=18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45
        self.jmp,self.jmc,self.jnc,self.jma,self.jna,self.jme,self.jne,self.jmz,self.jnz=48,50,51,52,53,54,55,56,57
        self.pxi,self.pxo,self.wri,self.wro,self.dsip=64,65,66,67,68
        self.ldva,self.ldvb,self.sdva,self.sdvb,self.sdv,self.ldck,self.sdck=96,97,98,99,100,101,102
        self.int1,self.int2,self.int3,self.int4,self.int4,self.int5,self.int6,self.int7,self.int8=128,129,130,131,132,133,134,135,136
        self.hlt=255
        self.addop,self.subop,self.andop,self.orop,self.xorop,self.shl,self.shr,self.inc,self.dec,self.cmpop,self.notop="000","001","010","011","100","0110","0111","1000","1001","11101","0101"
        self.gpuop,self.gsx,self.gsy,self.gs0,self.gs1,self.gsv,self.gwv="000","001","010","011","100","101","110"
        self.gdsp="123"
    def tick(self,clk,s,ram,stk,drv):
        self.gpuop="000"
        alut=""
        irv=num(self.ir.val)
        # print(irv)
        # if num(self.iar.val)>20:
        #     input("...")
        nop=irv==self.nop
        ad=num(self.marx.val)
        sd=num(self.sp.val)
        if s.s1:
            ram.mem[ad].e,self.ir.s=clk.e,clk.s
        if s.s2:
            self.iar.e,alut,self.acc.s=clk.e,self.inc,clk.s
        if s.s3:
            self.acc.e,self.iar.s,self.marx.s=clk.e,clk.s,clk.s
        if s.s4:
            if irv==self.hlt:return "HLT"
            elif irv in [self.lda,self.ldb,self.sta,self.stb]:ram.mem[ad].e,self.marx.s=clk.e,clk.s
            elif irv==self.nota:self.a.e,alut,self.acc.s=clk.e,self.notop,clk.s
            elif irv==self.notb:self.b.e,alut,self.acc.s=clk.e,self.notop,clk.s
            elif irv==self.shla:self.a.e,alut,self.acc.s=clk.e,self.shl,clk.s
            elif irv==self.shlb:self.b.e,alut,self.acc.s=clk.e,self.shl,clk.s
            elif irv==self.shra:self.a.e,alut,self.acc.s=clk.e,self.shr,clk.s
            elif irv==self.shrb:self.b.e,alut,self.acc.s=clk.e,self.shr,clk.s
            elif irv==self.inca:self.a.e,alut,self.acc.s=clk.e,self.inc,clk.s
            elif irv==self.incb:self.b.e,alut,self.acc.s=clk.e,self.inc,clk.s
            elif irv==self.incsp:self.sp.e,alut,self.acc.s=clk.e,self.inc,clk.s
            elif irv==self.deca:self.a.e,alut,self.acc.s=clk.e,self.dec,clk.s
            elif irv==self.decb:self.b.e,alut,self.acc.s=clk.e,self.dec,clk.s
            elif irv==self.decsp:self.sp.e,alut,self.acc.s=clk.e,self.dec,clk.s
            elif irv==self.psha:self.a.e,stk.mem[sd].s=clk.e,clk.s
            elif irv==self.pshb:self.b.e,stk.mem[sd].s=clk.e,clk.s
            elif irv==self.popa:self.a.s,stk.mem[sd].e=clk.s,clk.e
            elif irv==self.popb:self.b.s,stk.mem[sd].e=clk.s,clk.e
            elif irv in [self.pxi,self.pxo,self.wri]:self.gpu.s,self.x.e,self.gpuop=clk.s,clk.e,self.gsx#,self.lpxa,self.lpxb,self.spxa,self.spxb]:ram.mem[ad].e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsx
            # elif irv==self.wri:ram.mem[ad].e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsx#(self.gwv if clk.s else "000")
            elif (irv==self.jmp)or(irv==self.jmc and self.fc=="1")or(irv==self.jnc and self.fc=="0")or(irv==self.jmz and self.fz=="1")or(irv==self.jnz and self.fz=="0")or(irv==self.jme and self.fe=="1")or(irv==self.jne and self.fe=="0")or(irv==self.jma and self.fa=="1")or(irv==self.jna and self.fa=="0"):ram.mem[ad].e,self.marx.s,self.iar.s=clk.e,clk.s,clk.s
            elif irv==self.cpm:self.b.e,self.tmp.s=clk.e,clk.s
            # elif irv==self.axi:self.a.e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsx
            elif irv==self.call:self.iar.e,stk.mem[sd].s=clk.e,clk.e
            elif irv==self.ret:self.acc.s,stk.mem[sd].e,alut=clk.s,clk.e,self.inc
            # elif irv==self.ret:self.marx.s,self.iar.s,stk.mem[sd].e=clk.s,clk.s,clk.e
            elif irv==self.ldav:ram.mem[ad].e,self.a.s=clk.e,clk.s
            elif irv==self.ldbv:ram.mem[ad].e,self.b.s=clk.e,clk.s
            elif irv==self.int1 and clk.s:self.int.val=ktb[input("keyboard interupt!")]
            elif irv in[self.add,self.sub,self.ro,self.xor,self.nad]:self.b.e,self.tmp.s=clk.e,clk.s
            elif irv==self.dsip and clk.s:self.gpuop=self.gdsp
            elif irv==self.lxa:self.a.e,self.x.s=clk.e,clk.s
            elif irv==self.lya:self.a.e,self.y.s=clk.e,clk.s
            elif irv==self.lva:self.a.e,self.v.s=clk.e,clk.s
            elif irv==self.lxb:self.b.e,self.x.s=clk.e,clk.s
            elif irv==self.lyb:self.b.e,self.y.s=clk.e,clk.s
            elif irv==self.lvb:self.b.e,self.v.s=clk.e,clk.s
            elif irv==self.lxv:ram.mem[ad].e,self.x.s=clk.e,clk.s
            elif irv==self.lyv:ram.mem[ad].e,self.y.s=clk.e,clk.s
            elif irv==self.lvv:ram.mem[ad].e,self.v.s=clk.e,clk.s
        elif s.s5:
            if irv==self.lda:self.a.s,ram.mem[ad].e=clk.s,clk.e
            elif irv==self.ldb:self.b.s,ram.mem[ad].e=clk.s,clk.e
            elif irv==self.sta:self.a.e,ram.mem[ad].s=clk.e,clk.s
            elif irv==self.stb:self.b.e,ram.mem[ad].s=clk.e,clk.s
            elif irv in [self.nota,self.shla,self.shra,self.inca,self.deca]:self.acc.e,self.a.s=clk.e,clk.s
            elif irv in [self.notb,self.shlb,self.shrb,self.incb,self.decb]:self.acc.e,self.b.s=clk.e,clk.s
            elif irv in [self.incsp,self.decsp]:self.acc.e,self.sp.s=clk.e,clk.e
            
            elif irv in [self.jmp,(self.jmc if self.fc!="1" else self.jnc),(self.jmz if self.fz!="1" else self.jnz),(self.jme if self.fe!="1" else self.jne),(self.jma if self.fa!="1" else self.jna),self.lxv,self.lyv,self.lvv]:self.iar.e,alut,self.acc.s=clk.e,self.inc,clk.s
            elif irv in [self.pxi,self.pxo,self.wri]:self.gpu.s,self.y.e,self.gpuop=clk.s,clk.e,self.gsy
            # elif irv==self.axi:self.b.e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsy
            elif irv==self.call:ram.mem[ad].e,self.marx.s,self.iar.s=clk.e,clk.s,clk.s
            elif irv==self.ret:self.iar.s,self.acc.e,self.marx.s=clk.s,clk.e,clk.s
            elif irv==self.cpm:self.a.e,alut=clk.e,self.cmpop
            elif irv in[self.ldav,self.ldbv]:self.iar.e,self.acc.s,alut=clk.e,clk.s,self.inc
            elif irv==self.int1:ram.mem[ad].e,self.marx.s=clk.e,clk.s
            elif irv in[self.add,self.sub,self.ro,self.xor,self.nad]:self.a.e,alut,self.acc.s=clk.e,(self.addop if irv==self.add else(self.subop if irv==self.sub else(self.orop if irv==self.ro else (self.xorop if irv==self.xor else self.andop)))),clk.s
        elif s.s6:
            if irv in [self.lda,self.ldb,self.sta,self.stb]:self.iar.e,alut,self.acc.s=clk.e,self.inc,clk.s
            elif irv in [self.jmp,(self.jmc if self.fc!="1" else self.jnc),(self.jmz if self.fz!="1" else self.jnz),(self.jme if self.fe!="1" else self.jne),(self.jma if self.fa!="1" else self.jna),self.lxv,self.lyv,self.lvv]:self.iar.s,self.acc.e,self.marx.s=clk.s,clk.e,clk.s
            elif irv==self.wri:self.gpu.s,self.v.e,self.gpuop=clk.s,clk.e,(self.gwv if clk.s else "000")
            elif irv==self.pxi:self.gpuop,self.gpu.s,self.a.e=self.gs1,clk.s,clk.e
            elif irv==self.pxo:self.gpuop=self.gs0
            # elif irv==self.axi:self.gpuop=self.gs1
            elif irv in[self.ldav,self.ldbv,self.wri]:self.acc.e,self.marx.s,self.iar.s=clk.e,clk.s,clk.s
            elif irv==self.int1:ram.mem[ad].s,self.int.e=clk.s,clk.e
            elif irv in[self.add,self.sub,self.ro,self.xor,self.nad]:self.acc.e,self.a.s=clk.e,clk.s
        elif s.s7:
            if irv in [self.lda,self.ldb,self.sta,self.stb]:self.acc.e,self.iar.s,self.marx.s=clk.e,clk.s,clk.s
            # elif self.ir.val in [self.pxi,self.pxo,self.spxa,self.spxb]:ram.mem[ad].e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsy
            # elif self.ir.val==self.wri:ram.mem[ad].e,self.gpu.s,self.gpuop=clk.e,clk.s,self.gsy
            # elif self.ir.val==self.int1:self.iar.e,self.acc.s,alut=clk.e,clk.s,self.inc
        elif s.s8:
            # if self.ir.val in [self.pxi,self.pxo,self.lpxa,self.lpxb,self.spxa,self.spxb,self.int1]:self.iar.e,alut,self.acc.s=clk.e,self.inc,clk.s
            s.re=1
        elif s.s9:
            # if self.ir.val in [self.pxi,self.pxo,self.lpxa,self.lpxb,self.spxa,self.spxb,self.int1]:self.iar.s,self.acc.e,self.marx.s=clk.s,clk.e,clk.s
            # elif self.ir.val==self.wri:self.iar.e,self.acc.s,alut=clk.e,clk.s,self.inc
            pass
        elif s.s10:
            # if self.ir.val==self.pxi:self.gpuop=self.gs1
            # elif self.ir.val==self.pxo:self.gpuop=self.gs0
            # elif self.ir.val==self.spxa:self.gpu.s,self.a.e,self.gpuop=clk.s,clk.e,self.gsv
            # elif self.ir.val==self.spxb:self.gpu.s,self.b.e,self.gpuop=clk.s,clk.e,self.gsv
            # elif self.ir.val==self.wri:self.iar.s,self.marx.s,self.acc.e=clk.s,clk.s,clk.e
            # elif self.ir.val!=self.wri:s.re=1
            pass
            # elif self.ir.val==self.wri
        elif s.s11:
            # if self.ir.val==self.wri:ram.mem[ad].e,self.gpu.s,self.gpuop=clk.e,clk.s,(self.gwv if clk.s else "000")
            pass
        elif s.s12:
            # if self.ir.val==self.wri:self.iar.e,self.acc.s,alut=clk.e,clk.s,self.inc
            pass
        elif s.s13:
            # if self.ir.val==self.wri:self.iar.s,self.marx.s,self.acc.e=clk.s,clk.s,clk.e
            pass
        # print(ad)
        # print(ram.mem[ad])
        # print(ram.mem[ad].val)
        self.bus.st(self.a.ena(self.b.ena(self.sp.ena(self.marx.ena(self.ir.ena(self.iar.ena(self.acc.ena(ram.mem[ad].ena(stk.mem[sd].ena(self.gpu.ena(self.int.ena(self.x.ena(self.y.ena(self.v.ena(REG().val)))))),clk.e),clk.e),clk.e),clk.e),clk.e),clk.e),clk.e),clk.e))
        self.a.st(self.bus.val,clk.s)
        self.b.st(self.bus.val,clk.s)
        self.sp.st(self.bus.val,clk.s)
        self.marx.st(self.bus.val,clk.s)
        self.ir.st(self.bus.val,clk.s)
        self.iar.st(self.bus.val,clk.s)
        self.acc.st(self.alu(alut),clk.s)
        self.gpu.st(self.bus.val)
        self.tmp.st(self.bus.val)
        self.x.st(self.bus.val)
        self.y.st(self.bus.val)
        self.v.st(self.bus.val)
        ram.mem[ad].st(self.bus.val,clk.s)
        stk.mem[sd].st(self.bus.val)
    def alu(self,op):
        # op=num(("0"*(16-len(op)))+op)
        # print(op)
        a=self.bus.val
        b=self.tmp.val
        # print(a)
        # print("|"+op+"|",a,b)
        # print(op,a,b)
        if op==self.inc:
            b=byt(1)
            op="add"
        elif op==self.dec:
            b=byt(1)
            op="sub"
        if op==self.notop:
            self.fc="0" 
            return "".join([str(nt(i)) for i in a])
        elif op==self.shl:
            self.fc=a[0]
            return a[1:]+"0"
        elif op==self.shr:
            self.fc=a[len(a)-1]
            return "0"+a[:len(a)-1]
        elif op==self.addop:
            # input("add")
            return ula.oper(a,b,"0","add")[0]
        elif op==self.subop:
            return ula.oper(a,b,"0","sub")[0]
        elif op==self.andop:
            return "".join([str(int(int(a[i]) and int(b[i]))) for i in range(len(a))])
        elif op==self.orop:
            return "".join([str(int(int(a[i]) or int(b[i]))) for i in range(len(a))])
        elif op==self.xorop:
            return "".join([XOR(a[i],b[i]) for i in range(len(a))])
        elif op==self.cmpop:
            # print(self.fc+self.fa+self.fe+self.fz)
            self.fc="1" if num(a)+num(b)>=2**16 else "0"
            self.fa="1" if num(a)>num(b) else "0"
            self.fe="1" if num(a)==num(b) else "0"
            self.fz="0" if "1" in a else "1"
    def display(self,clk,s,ram,stk):
        # print("\033c",end="")
        ad=num(self.marx.val)
        sd=num(self.sp.val)
        # print(sd)
        # print(f"clk: {clk.c} | clks:{clk.s} | clke:{clk.e} | clkd: {clk.d}")
        # print(f"S1:{s.s1}|S2:{s.s2}|S3:{s.s3}|S4:{s.s4}|S5:{s.s5}|S6:{s.s6}|S7:{s.s7}|S8:{s.s8}|S9:{s.s9}|S10:{s.s10}|S11:{s.s11}")
        # print(f"  a:{self.a}|")
        registerDisp(200,20,self.b.val,"b")
        # print(f"  b:{self.b}|")
        # print(f"mar:{self.marx}|")
        # print(f" ir:{self.ir}|")
        # print(f"iar:{self.iar}|")
        # # print(self.acc)
        # print(f"acc:{self.acc}|")
        # print(f"tmp:{self.tmp}|")
        # print(f"bus:{self.bus}|")
        # print(f"ram:{ram.mem[ad]}|")
        # print(f" sp:{self.sp}|")
        # print(sd)
        # print(f"stk:{stk.mem[sd]}|")
        # print(f"gpu:{self.gpu}|")
        # print(f"int:{self.int}|")
        # print(f"  x:{self.x}|")
        # print(f"  y:{self.y}|")
        # print(f"  v:{self.v}|")
        # print(self.fc+self.fa+self.fe+self.fz)
    def disp(self,ram,stk):
        ad,sd=num(self.marx.val),num(self.sp.val)
        str(self.a)+str(self.b)+str(self.marx)+str(self.ir)+str(self.iar)+str(self.acc)+str(self.tmp)+str(ram.mem[ad])+str(self.sp)+str(stk.mem[sd])+str(self.gpu)+str(self.int)+str(self.x)+str(self.y)+str(self.v)

#ram.mem[ad].e=0011_0xxx,s4 or 0100_0xxx,s4 or 0000_0xxx,s4 or 0000_001x,s5 and not 0000_011x
#gpu.s=[0100_0xxx,s4 or s7
#stk.e=(0001_010x,s4
#stk.s=0001_011x,s4
#acc.e=0000_1xxx,s5 or 0001_00xx,s5 or 0010_000x,s5 or 0000_0xxx,s7 and not 0000_011x or 0000_100x
#{
        # print(ad,sd)
        #lda/b->get addr,store to mar;enable ram, set a/b
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
        
        # irv=self.ir.val
        # #=()and clk. and not(nop),(cm(irv,"")and s.s)or
        # ram.mem[ad].e=(s.s1 or(cm(irv,"0011_0xxx")and s.s4)or(cm(irv,"0100_0xxx")and s.s4)or(cm(irv,"0000_0xxx")and s.s4)or(cm(irv,"0000_001x")and s.s5))and clk.e and not(cm(irv,"0000_011x")or nop)
        # self.iar.e=(s.s2 )and clk.e and not(nop)
        # self.acc.e=(s.s3 or(cm(irv,"0000_1xxx")and s.s5)or(cm(irv,"0001_00xx")and s.s5)or(cm(irv,"0010_000x")and s.s5)or(cm(irv,"0000_0xxx")and s.s7)or)and clk.e and not(nop or cm(irv,"000_011x")or cm(irv,"0000_100x"))
        # stk.mem[sd].e=cm(irv,"0001_010x") and s.s4 and clk.e and not(nop)
        # self.sp.e=()and clk.e and not(nop)
        # self.a.e=()and clk.e and not(nop)
        # self.b.e=()and clk.e and not(nop)
        
        # self.iar.s=(s.s3 )and clk.s and not(nop)
        # self.ir.s=(s.s1 )and clk.s and not(nop)
        # self.acc.s=(s.s2 or(cm(irv,"0000_1xxx")and s.s4)or(cm(irv,"0001_00xx")and s.s4)or(cm(irv,"0010_000x")and s.s4)or(cm(irv,"0100_0xxx")and s.s5)or(cm(irv,"0011_0xxx")and s.s5)or(cm(irv,"")and s.s)or)and clk.s and not(nop)
        # self.marx.s=(s.s3 )and clk.s and not(nop)
        # self.gpu.s=cm(irv,"0100_0xxx")and(s.s4 or s.s7)and clk.s and not(nop)
        # stk.mem[sd].s=cm(irv,"0001_011x") and s4 and clk.s and not(nop)
        # self.sp.s=()and clk.s and not(nop)
        # self.a.s=()and clk.s and not(nop)
        # self.b.s=()and clk.s and not(nop)
        
        # alut=(self.inc if s.s2 else "")
        # if s.s4:
        #     if self.ir.val==self.hlt:return "HLT"
        #     elif self.ir.val in [self.lda,self.ldb,self.sta,self.stb]:ram.mem[ad].e,self.marx.s=clk.e,clk.s
        #     elif self.ir.val in [self.nota,self.notb]:alut=self.ont
        #     elif self.ir.val in [self.shla,self.shlb]:alut=self.shl
        #     elif self.ir.val in [self.shra,self.shrb]:alut=self.shr
        #     elif self.ir.val in [self.inca,self.incb,self.incsp]:alut=self.inc
        #     elif self.ir.val in [self.deca,self.decb,self.decsp]:alut=self.dec
        #     elif self.ir.val in [self.pxi,self.pxo,self.lpxa,self.lpxb,self.spxa,self.spxb]:self.gpuop=self.gsx
        #     elif self.ir.val==self.wri:self.gpuop=(self.gwv if clk.s else "000")
        #     elif self.ir.val=="000"+self.cpm:alut=self.cpm
        # elif s.s5:
        #     if self.ir.val in [self.pxi,self.pxo,self.lpxa,self.lpxb,self.spxa,self.spxb,self.wri,self.jmp,(self.jmc if self.fc!="1" else ""),(self.jnc if self.fc=="1" else ""),(self.jmz if self.fz!="1" else ""),(self.jnz if self.fz=="1" else "")]:alut=self.inc
        # elif s.s6:
        #     if self.ir.val in [self.lda,self.ldb,self.sta,self.stb]:alut=self.inc
        # elif s.s7:
        #     if self.ir.val==self.pxi:self.gpuop=self.gs1
        #     elif self.ir.val==self.pxo:self.gpuop=self.gs0
        #     elif self.ir.val==self.spxa:self.gpuop=self.gsv
        #     elif self.ir.val==self.spxb:self.gpuop=self.gsv
        #}