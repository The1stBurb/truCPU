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
    def adder(self,a,b,c):
        a,b,c=int(a),int(b),int(c)
        return str(logic.XOR(logic.XOR(a,b),c)),str(logic.OR(logic.AND(a,b),logic.AND(c,logic.XOR(a,b))))
    def adder4(self,a,b,c):
        s3,c3=self.adder(a[3],b[3],c)
        s2,c2=self.adder(a[2],b[2],c3)
        s1,c1=self.adder(a[1],b[1],c2)
        s0,c0=self.adder(a[0],b[0],c1)
        return s0+s1+s2+s3,c0
    def adder16(self,a,b,c):
        s3,c3=self.adder4(a[12:],b[12:],c)
        s2,c2=self.adder4(a[8:12],b[8:12],c3)
        s1,c1=self.adder4(a[4:8],b[4:8],c2)
        s0,c0=self.adder4(a[:4],b[:4],c1)
        return s0+s1+s2+s3,c0
    def invert(self,a):return "".join([str(logic.NOT(int(i))) for i in a])
    def oper(self,a,b,c,op):
        if op=="add":
            return self.adder16(a,b,c)
        elif op=="sub":
            return self.adder16(a,self.invert(b),"1")