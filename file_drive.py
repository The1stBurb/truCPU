from DRIVE import DRIVE
import os
files=["CrimsonTreeOS.img"]
drv=DRIVE()
for i in range(len(files)):
    if files[i]=="":continue
    dat=""
    with open(f"codeFiles/{files[i]}","r")as fil:
        dat=fil.read()
    drv.build(dat,i)