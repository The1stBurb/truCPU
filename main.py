from time import sleep
from RAM import RAM
from CPU import CPU
from GPU import GPU
from register import STPR,STACK,CLK
from assemb import mac
ram=RAM().build(mac)
cpu=CPU()
gpu=GPU()
clk=CLK()
stp=STPR()
stk=STACK()
# print(not 1)
# input()
gpu.display(())
while True:
    # print("\033c",end="")
    # print(ram)
    # try:
    clk.tick()
    stp.tick(clk)
    if cpu.tick(clk,stp,ram,stk)=="HLT":
        break
    cpu.disp(ram,stk)
    gpu.tick(clk,stp,cpu.gpu.val,cpu.gpuop,(cpu.fc,cpu.fa,cpu.fe,cpu.fz))
    # except:
    #     cpu.display(clk,stp,ram,stk)
    #     input()
    # cpu.bus.st(gpu.mem[gpu.ad].ena(cpu.bus.val))
    # gpu.display()
    # sleep(0.01)
    # input()
    # print("r",end="")
gpu.display(())
cpu.display(clk,stp,ram,stk)
# print(ram.mem[len(mac)-1].val)
print("HALTED!")
# print(ram.mem[:20])