from allVars import driveSize,diskSize,sectorSize,sliceSize
from register import REG
from allFuncs import num,byts,hex_bin
import os
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
    return [REG()for i in range(2**16)]
class DRIVE:
    def __init__(self):
        self.mem=[FILE()for i in range(diskSize)]#[[SECTOR() for i in range(diskSize)] for i in range(driveSize)]
        self.loc="0"*8
        self.e=False
        self.s=False
        # self.d2=[SECTOR() for i in range(diskSize)]
        # self.d3=[SECTOR() for i in range(diskSize)]
        # self.d4=[SECTOR() for i in range(diskSize)]
        # self.d5=[SECTOR() for i in range(diskSize)]
        # self.fl=os.listdir()
    def st(self,bus):
        self.cur().st(bus)
    def ena(self,bus,addr=0):
        se=self.e
        self.e=False
        return self.cur(addr).val if se else bus
    # def cur(self):
    #     diskLoc=num(self.loc[0:4])
    #     sectorLoc=num(self.loc[4:8])
    #     sliceLoc=num(self.loc[8:12])
    #     memLoc=num(self.loc[12:16])
    #     return self.mem[diskLoc][sectorLoc][sliceLoc][memLoc]
    def cur(self,addr=0):
        # input(addr,num(self.loc))
        return self.mem[num(self.loc)][addr]
    def __str__(self):
        s,e=self.cur().s,self.cur().e
        return str(self.cur().val)+f"|s:{s}|e:{e}"
    def build(self,dat,file):
        # input(f"file: {file}")
        for i in range(0,len(dat),4):
            # input(f"{i//4} , {len(self.mem[file])} , {dat[i:i+4]} {hex_bin("".join(dat[i:i+4]))}")
            self.mem[file][i//4].val=hex_bin("".join(dat[i:i+4]))
        # input(self.mem[file][:10])
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