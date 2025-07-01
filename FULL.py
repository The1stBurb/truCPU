from CPU import CPU,num
from GPU import GPU
from RAM import RAM
from file_drive import drv
from register import STPR,STACK,CLK
from assemb import mac
class COMPUTER:
    def __init__(self):
        self.ram=RAM().build(mac)                                    
        self.cpu=CPU()
        self.gpu=GPU()
        self.clk=CLK()
        # drv=DRIVE()
        self.stp=STPR()
        self.stk=STACK()
        self.gpu.display(())
    def run(self,start,kbrd):
        # while True:
        self.clk.tick()
        self.stp.tick(self.clk)
        cpuRet=self.cpu.fastTick(self.ram,self.stk,drv,self.gpu,start,kbrd)#
        # cpuRet=cpu.tick(self.clk,self.stp,self.ram,self.stk,drv)
        if cpuRet=="HLT":
            return "HLT"
        self.cpu.disp(self.ram,self.stk)
        self.gpu.tick(self.clk,self.stp,self.cpu.gpu.val,self.cpu.gpuop,(self.cpu.fc,self.cpu.fa,self.cpu.fe,self.cpu.fz))
        print(f"running addr:{num(self.cpu.marx.val)}|{self.clk}|{self.stp.cur()}",end="\r")

class KEYBOARD:
    def __init__(self):
        self.kys=[]
    def getKey(self):
        if len(self.kys)==0:return 0
        self.kys=[self.kys[-1]]
        return self.kys.pop()
    def readKey(self,ky):
        if ky==1073741906:ky=40
        elif ky==1073741903:ky=41
        elif ky==1073741905:ky=51
        elif ky==1073741904:ky=50
        self.kys.append(ky)
#have a "ram" that every time a key is pressed, it saves it in ram and moves mem loc up and opposite for get key.
class MOUSE:
    def __init__(self):
        self.msx=0
        self.msy=0
        self.lftPrs=False
        self.midPrs=False
        self.rgtPrs=False
#store mouse data