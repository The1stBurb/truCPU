from time import sleep,perf_counter_ns
from RAM import RAM
from CPU import CPU,num
from GPU import GPU
from DRIVE import DRIVE
from register import STPR,STACK,CLK
from assemb import mac
ram=RAM().build(mac)
cpu=CPU()
gpu=GPU()
clk=CLK()
drv=DRIVE()
stp=STPR()
stk=STACK()
# print(not 1)
# input()
start=perf_counter_ns()
while True:
    # print("\033c",end="")
    # print(ram)
    # try:
    clk.tick()
    stp.tick(clk)
    if cpu.tick(clk,stp,ram,stk,drv)=="HLT":
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
    print(f"running addr:{num(cpu.marx.val)}|{clk}|{stp.cur()}",end="\r")
    # if clk.s and stp.s1:input("fish")
end=perf_counter_ns()
gpu.display(())
cpu.display(clk,stp,ram,stk)
# print(ram.mem[len(mac)-1].val)
print("HALTED!")
print(f"took {(end-start)/1_000_000} ms")
# print(ram.mem[:20])

# & C:/Users/ECoop/AppData/Local/Programs/Python/Python313/python.exe c:/Users/ECoop/Desktop/truCPU/main.py