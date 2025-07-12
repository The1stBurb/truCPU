from coding import asembly
from allFuncs import byt,COLOUR
from allVars import ltrs,ltr
ops={
    "nop":0,
    "lda":2,"ldb":3,"ldav":4,"ldbv":5,"sta":6,"stb":7,"lxa":8,"lxb":9,"lya":10,"lyb":11,"lva":12,"lvb":13,"lxv":14,"lyv":15,"lvv":16,
    "nota":18,"notb":19,"shla":20,"shlb":21,"shra":22,"shrb":23,"inca":24,"incb":25,"deca":26,"decb":27,"add":28,"sub":29,"or":30,"xor":31,"psha":32,"pshb":33,"popa":34,"popb":35,"lpxa":36,"lpxb":37,"spxa":38,"spxb":39,"incsp":40,"decsp":41,"call":42,"ret":43,"cmp":44,"and":45,
    "jmp":48,"jmc":50,"jnc":51,"jma":52,"jna":53,"jme":54,"jne":55,"jmz":56,"jnz":57,
    "pxi":64,"pxo":65,"wri":66,"wro":67,"disp":68,"sclr":69,"pxg":70,
    "ldva":96,"ldvb":97,"sdva":98,"sdvb":99,"sdv":100,"ldck":101,"sdck":102,
    "int1":128,"int2":129,"int3":130,"int4":131,"int5":132,"int6":133,"int7":134,"int8":135,
    "hlt":255,
    "ldca":300,"stid":301,
    "dbg":456,"dbg1":457,
}
#repr(input("fish>"))
# asembly="""
# nop
# call rdky;2
# call wrtky;4
# call nl;6
# jmp #0;8
# hlt;9
# #34;latest char 10
# #0;cursor pos 11
# #0;cursor y 12
# rdky:
#  int1 #10;read key to latest char 14
#  lda #10;load to a from latest char 16
#  ret;17
# wrtky:
#  lda #10;load to a from latest char 19
#  sta #33;21
#  lda #11;load cursor position to a 23
#  sta #31;to x of above wrt 25
#  lda #12;27
#  sta #32;29
#  wrt #0 #0 _;write it 33
#  inca;increment 34
#  inca;again 35
#  inca;yep 36
#  inca;this makes it 4x spaces, the right space for next char 37
#  sta #11;store it to cursor pos 39
#  ret;40
# nl:
#  ldbv #61;42
#  lda #11;44
#  sta #50;46
#  wrt #56 #12 A
#  cmp;45
#  jma #77;47
#  lda #12;49
#  ldbv #6;51
#  add;52
#  sta #12;54
#  ldav #0;56
#  sta #11;58
#  nop;59
#  lda #72;61
#  inca;62
#  sta #72;64
#  sta #70;66
#  wrt #60 #12 #1;70
#  nop
#  ret;71
# #1;72
# """
# asembly="""
# loop:
#  incsp
#  int1 00010000     ; wait for key, store at RAM[00001100]
#  lda 00010000      ; load key into a
#  lva               ; set v = a
#  ldav 00000000     ; load 0 into a
#  lxa               ; x = 0
#  lya               ; y = 0
#  wri; write character v to (x,y)
#  decsp
# ret
# nop
# call loop
# hlt
# """
# asembly="""
# ldca #0
# lxa
# ldav #0
# lya
# lda #4095
# pxi
# disp
# """
lines = asembly.split("\n")
if lines[-1]!="hlt":
    lines.append("hlt")
stats = {}
lvl2 = []
mac = []
# print(lines)
for line in lines:
    line = line.strip()
    print(" "*40,line," "*3,end="\r")
    if not line or line.startswith(";"):
        continue

    if ";" in line:
        line = line.split(";", 1)[0].strip()

    if ":" in line:
        label = line.rstrip(":")
        stats[label] = len(mac)
        continue

    if line.startswith("#"):
        value = line[1:]
        lvl2.append(value)
        # if value in ltrs:mac.append(byt(ltrs[value]))
        # else:
        mac.append(value.replace("_", "") if "_" in value else byt(int(value)))
        continue
    elif line.startswith("'"):
        v=line[1:]
        mac.append(byt(ltrs[v]))
        continue

    tokens = line.split()
    # print(tokens)
    op = tokens[0]

    if op not in ops:
        continue

    lvl2.append(op)
    # if op=="ldca":input("ldca"+str(ops[op]))
    mac.append(byt(ops[op]))

    for arg in tokens[1:]:
        lvl2.append(arg)
        if arg in ltrs:
            mac.append(byt(ltrs[arg]))
        elif arg.startswith("'"):
            b=byt(ltrs[arg[1:]])
            mac.append(b)
        elif arg.startswith("\""):
            mac.append(byt(ltr.index(arg[1])))
        elif arg.startswith("#"):
            # if arg[1:]in ltrs:
            #     mac.append(byt(ltrs[arg[1:]]))
            # else:
            b=byt(int(arg[1:]))
            if isinstance(b,list):mac.extend(b)
            else:mac.append(b)
        elif "col"in arg:
            b=arg.split(",")
            mac.append(byt(COLOUR(int(b[1]),int(b[2]),int(b[3]))))
        else:
            mac.append(arg.replace("_", ""))

# Resolve label references
for idx, code in enumerate(mac):
    # if code==byt(300):input("ldca2")
    if code in stats:
        mac[idx] = byt(stats[code])
# if [300] in mac:print("ldca")
# print(mac,len(mac))
# quit()
# input()