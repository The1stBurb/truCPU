from time import sleep,perf_counter_ns
import pygame
from FULL import COMPUTER,KEYBOARD
kbrd=KEYBOARD()
# print(not 1)
# input()
cmr=COMPUTER()
start=perf_counter_ns()
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()
        elif i.type==pygame.KEYDOWN:
            kbrd.readKey(i.key)
            # print("\n",i.key)
    cmrOut=cmr.run(start,kbrd)
    # input()
    if cmrOut=="HLT":break
end=perf_counter_ns()
cmr.gpu.display(())
cmr.cpu.display(cmr.clk,cmr.stp,cmr.ram,cmr.stk)
# print(ram.mem[len(mac)-1].val)
print("HALTED!")
print(f"took {(end-start)/1_000_000} ms")
# print(ram.mem[:20])
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()
# & C:/Users/ECoop/AppData/Local/Programs/Python/Python313/python.exe c:/Users/ECoop/Desktop/truCPU/main.py