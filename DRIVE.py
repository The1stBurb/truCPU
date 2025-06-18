from allVars import driveSize,diskSize,sectorSize,sliceSize
from register import REG
from allFuncs import num,byts,hex_bin
# class 
def SLICE():
    # def __init__(self):
        # self.mem=
    return [REG()for i in range(sliceSize)]
# class 
def SECTOR():
    # def __init__(self):
        # self.mem=
    return [SLICE() for j in range(sectorSize)]
def FILE():
    return [REG()for i in range(2**10)]
class DRIVE:
    def __init__(self):
        self.mem=[FILE()for i in range(diskSize)]#[[SECTOR() for i in range(diskSize)] for i in range(driveSize)]
        self.loc="0"*8
        # self.d2=[SECTOR() for i in range(diskSize)]
        # self.d3=[SECTOR() for i in range(diskSize)]
        # self.d4=[SECTOR() for i in range(diskSize)]
        # self.d5=[SECTOR() for i in range(diskSize)]
    def st(self,bus):
        self.cur().st(bus)
    def ena(self,bus):
        return self.cur().ena(bus)
    # def cur(self):
    #     diskLoc=num(self.loc[0:4])
    #     sectorLoc=num(self.loc[4:8])
    #     sliceLoc=num(self.loc[8:12])
    #     memLoc=num(self.loc[12:16])
    #     return self.mem[diskLoc][sectorLoc][sliceLoc][memLoc]
    def cur(self,addr=0):
        return self.mem[num(self.loc)][addr]
    def __str__(self):
        s,e=self.cur().s,self.cur().e
        return str(self.cur())+f"|s:{s}|e:{e}"
    def build(self,dat,file):
        for i in range(0,len(dat),2):
            self.mem[file][i//2]=hex_bin(dat[i]+dat[i+1])
#img - width height data seperated by 2^15,#txt-just
#16 bits 0000DISK 0000SECTOR 0000SLICE 0000MEMloc ig
# drv=DRIVE()
# print(drv)
# drv.cur().s=1
# drv.st("0000000000000001")
# print(drv)
# drv.loc=("0"*7)+"1"
# print(drv)
# drv.cur().s=1
# drv.st("0000000000000010")
# print(drv)