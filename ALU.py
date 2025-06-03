from allFuncs import num
class LogicGates:
    def __init__(self):pass
    def OR(self,a,b):return int(self.NAND(self.NAND(a,a),self.NAND(b,b)))
    def XOR(self,a,b):return int(self.AND(self.OR(a,b),self.NAND(a,b)))
    def AND(self,a,b):return int(self.NOT(self.NAND(a,b)))
    def NAND(self,a,b):return int(not(a and b))
    def NOT(self,a):return int(self.NAND(a,a))
logic=LogicGates()
class ALU:
    def __init__(self):pass
    def adder(self,a,b,c,sp):
        a,b,c=int(a),int(b),int(c)
        s=str(logic.XOR(logic.XOR(a,b),c))
        co=str(logic.OR(logic.AND(a,b),logic.AND(c,logic.XOR(a,b))))
        for i in sp:
            if "="in i:
                if i[0]=="s":s=co
            elif "x"in i:
                if i[1]=="c":co="0"
            elif "!"in i:
                if i[1]=="s":s=str(logic.NOT(int(s)))
            elif "+"in i:
                s=str(logic.OR(int(s),int(co)))
        return s,co
    def adder4(self,a,b,c,sp=[]):
        s3,c3=self.adder(a[3],b[3],c,sp)
        s2,c2=self.adder(a[2],b[2],c3,sp)
        s1,c1=self.adder(a[1],b[1],c2,sp)
        s0,c0=self.adder(a[0],b[0],c1,sp)
        return s0+s1+s2+s3,c0
    def adder16(self,a,b,c,sp=[]):
        s3,c3=self.adder4(a[12:],b[12:],c,sp)
        s2,c2=self.adder4(a[8:12],b[8:12],c3,sp)
        s1,c1=self.adder4(a[4:8],b[4:8],c2,sp)
        s0,c0=self.adder4(a[:4],b[:4],c1,sp)
        return s0+s1+s2+s3,c0
    def invert(self,a):return "".join([str(logic.NOT(int(i))) for i in a])
    def oper(self,a,b,c,op):
        if op=="add":
            return self.adder4(a,b,c)
        elif op=="sub":
            return self.adder16(a,self.invert(b),"1")
        elif op=="and":
            #and-11-1
            return self.adder4(a,b,"0",sp=["s=c","xc"])
        elif op=="xor":
            return self.adder4(a,b,"0",sp=["xc"])
        elif op=="or":
            return self.adder4(a,b,c,sp=["+","xc"])
        elif op=="not":
            return self.adder4(a,b,"0",sp=["!s"])
alu=ALU()
a="0110"
b="0000"
c="1"
print(alu.oper(a,b,c,"add"))
print(alu.oper(a,b,c,"and"))
print(alu.oper(a,b,c,"xor"))
print(alu.oper(a,b,c,"or"))
print(alu.oper(a,b,c,"not"))