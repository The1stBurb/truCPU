from allVars import ltr
from CPU import CPU,num
from GPU import GPU
from RAM import RAM
from file_drive import drv
from register import STPR,STACK,CLK
from assemb import mac
# from pygame import
# import pygame 
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
        print(f"|{self.clk}|{self.stp.cur()}|            running addr:{num(self.cpu.marx.val)}      ",end="\r")

class KEYBOARD:
    def __init__(self):
        self.kys=[]
        self.shft=False
    def getKey(self):
        if len(self.kys)==0:return 0
        self.kys=[self.kys[-1]]
        return self.kys.pop()
    def readKey(self,ky):
        if ky=="up":ky=100
        elif ky=="right":ky=101
        elif ky=="down":ky=102
        elif ky=="left":ky=103
        elif ky=="shift":
            self.shft=True
            return
        elif ky=="space":ky=" "
        elif ky=="return":ky=105
        if self.shft:
            self.shft=False
            ky=ky.upper()
        # elif ky==pygame.
        # input(ky)
        # if ky==" ":input(ky+str(ltr.index(ky)))
        if isinstance(ky,int):self.kys.append(ky)
        elif ky in ltr:self.kys.append(ltr.index(ky))
#have a "ram" that every time a key is pressed, it saves it in ram and moves mem loc up and opposite for get key.
class MOUSE:
    def __init__(self):
        self.msx=0
        self.msy=0
        self.lftPrs=False
        self.midPrs=False
        self.rgtPrs=False
#store mouse data
# kys=KEYBOARD()
# while True:
#     for i in pygame.event.get():
#         if i.type==pygame.KEYDOWN:
#             kys.readKey(i.key)
#             print(i.key)
#-435, 67, 2354