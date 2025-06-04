from allVars import stkSize
from allFuncs import byts,bitSize
class REG:
    def __init__(self,always_set=False):
        self.val=str("0"*bitSize)
        self.als=int(always_set)
        self.s=self.als
        self.e=0
        self.s2=0
        self.e2=0
    def st(self,val,clks=1):
        # print(self.s,clks)
        self.s2=self.s
        if self.s and val!=None:# and clks 
            self.val=val
            # self.s=self.als
    def ena(self,busPass,clke=1):
        self.e2=self.e
        if self.e:# and clke
            # self.e=0
            return self.val
        return busPass
    def __str__(self):
        s,e=self.s,self.e
        self.s=self.als
        self.e=0
        return byts(self.val)+f"|s:{s}|e:{e}"
    def __repr__(self):
        return self.val

class STACK:
    def __init__(self):
        self.mem=[REG() for i in range(stkSize)]
    def build(self,mem):
        ad=0
        for i in mem:
            self.mem[ad].s=1
            self.mem[ad].st(i)
            self.mem[ad].s=0
            ad+=1
        return self
    def cur(self,addr):
        return self.mem[addr]
    def __repr__(self):
        return str([str(i.val)for i in self.mem])

class STPR:
    def __init__(self):
        self.s1=self.s2=self.s3=self.s4=self.s5=self.s6=self.s7=self.s8=self.s9=self.s10=self.s11=self.s12=0
        self.s13=1
        self.re=0
    def tick(self,clk):
        if self.re:
            self.s1=self.s2=self.s3=self.s4=self.s5=self.s6=self.s7=self.s8=self.s9=self.s10=self.s11=self.s12=0
            self.s13=1
            self.re=0
        if not(clk.c or clk.d):
            self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.s10,self.s11,self.s12,self.s13=self.s13,self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.s10,self.s11,self.s12
    def __str__(self):
        return f"1:{self.s1}|2:{self.s2}|3:{self.s3}|4:{self.s4}|5:{self.s5}|6:{self.s6}|7:{self.s7}|8:{self.s8}|9:{self.s9}|10:{self.s10}|11:{self.s11}|12:{self.s12}|"
    def cur(self):
        for x,i in enumerate([self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9,self.s10,self.s11,self.s12]):
            if i:return str(x+1)
        return "0"

class CLK:
    def __init__(self):
        self.count=0
        self.c=0
        self.d=0
        self.e=0
        self.s=0
    def tick(self):
        self.count+=1
        if self.count==4:
            self.c=0
            self.count=0
        elif self.count==3:self.d=1
        elif self.count==2:self.c=1
        elif self.count==1:self.d=0
        self.s,self.e=self.c and self.d,self.c or self.d
    def __str__(self):
        return f"c:{self.c}|d:{self.d}|s:{self.s}|e:{self.e}"