from code import asembly,byt
ops={
    "nop":0,
    "lda":2,"ldb":3,"ldav":4,"ldbv":5,"sta":6,"stb":7,"lxa":8,"lxb":9,"lya":10,"lyb":11,"lva":12,"lvb":13,"lxv":14,"lyv":15,"lvv":16,
    "nota":18,"notb":19,"shla":20,"shlb":21,"shra":22,"shrb":23,"inca":24,"incb":25,"deca":26,"decb":27,"add":28,"sub":29,"or":30,"xor":31,"psha":32,"pshb":33,"popa":34,"popb":35,"lpxa":36,"lpxb":37,"spxa":38,"spxb":39,"incsp":40,"decsp":41,"call":42,"ret":43,"cmp":44,
    "jmp":48,"jmc":50,"jnc":51,"jma":52,"jna":53,"jme":54,"jne":55,"jmz":56,"jnz":57,
    "pxi":64,"pxo":65,"wri":66,"wro":67,"disp":68,
    "int1":128,"int2":129,"int3":130,"int4":131,"int5":132,"int6":133,"int7":134,"int8":135,
    "hlt":255,
    # "ldac":"0000_0110","ldbc":"0000_0111","stac":"0000_1000","stbc":"0000_1001","nota":"0000_1010","notb":"0000_1011","shlb":"0000_1101","shla":"0000_1100","shrb":"0000_1111","shra":"0000_1110","incb":"0001_0001","inca":"0001_0000","decb":"0001_0011","deca":"0001_0010","popb":"0001_0101","popa":"0001_0100","psha":"0001_0110","pshb":"0001_0111","add":"0001_1000","sub":"0001_1001","and":"0001_1010","or":"0001_1011","xor":"0001_1100","cmp":"0001_1101","swap":"0001_1110","ldav":"0010_0100","ldbv":"0010_0101",# "jmp":"0011_0000","jmz":"0011_0010","jnz":"0011_0011","jmc":"0011_0100","jnc":"0011_0101","jme":"0011_0110","jne":"0011_0111","jma":"0011_1000","jna":"0011_1001","call":"0011_1010","ret":"0011_1111",# "incsp":"0010_0000","decsp":"0010_0001","push":"0010_0010","pop":"0010_0011",# "pxi":"0100_0000","pxo":"0100_0001","lpxa":"0100_0010","lpxb":"0100_0011","spxa":"0100_0100","spxb":"0100_0101","wrt":"0100_0110","axi":"0100_1000",# "hlt":"1000_0000","sxa":"1000_0010","sxb":"1000_0011","sya":"1000_0100","syb":"1000_0101","sva":"1000_0110","svb":"1000_0111",# "int1":"1000_1000","int2":"1000_1001"
#int1-keyboard,int2-mouse
#nop - do nothing
#ld(a or b) addr - set a or b from the address in ram
#st(a or b) addr - set the address in ram from a or b
#not(a or b) - not a or b and set to a or b
#shl(a or b) - shift a or b left and set to a or b
#shr(a or b) - shift a or b right and set to a or b
#lx(a or b) - set the x register with a or b
#ly(a or b) - set the y register with a or b
#lv(a or b) - set the v register with a or b
#inc(a or b or sp) - increment a or b or stack pointer and set to a or b or stack pointer
#dec(a or b or sp) - decrement a or b or stack pointer and set to a or b or stack pointer
#psh(a or b) - push a or b onto stack (does not increment the stack pointer)
#pop(a or b) - take whts on the stack and store into a or b (does not decrement the stack pointer)
#add, sub, or, xor - does this alu op and stores to a, i.e. for add a+b->a
#cmp - compares a and b, sets flags
#ld(a or b)v value - load value into a or b
#jmp addr - jump to address plus 1
#thes are jump ops based of flags: jmz - jump if Zero, jnz - jump if not Zero, jmc - jump if CarryOut, jnc - jump if not CarryOut, jme - jump if Equal, jne - jump if not Equal, jma - jump if ALarger, jna - jump if not ALarger
#pxi - turns on pixel and sets VRAM to 1 at register x,register y (X,Y)
#pxo - turns off pixel and sets VRAM to 0 at register x,register y (X,Y)
#wri - puts a character and sets VRAM for pixels of char at ofsets from register x,register y (X,Y). register v is char.
#int1 addr - wait for key input from user, store to ram at address
#int2 addr - read mouseX, store to ream at address
#int3 addr - read mouseY, store to ream at address
#int4 addr - read mouseLeftButton (0 not pressed, 1 pressed), store to ream at address
#int6 addr - read mouseRightButton (0 not pressed, 1 pressed), store to ream at address
#to use a number value do #num; to use single char do 'char; commnet is ";"
#VRAM size is 21x68, seperate from RAM
#RAM size is 256*256
#stack size is 32, seperate from RAM
#changeable registers - sp, a, b, x, y, v
}
ltrs={
    "A":33,"B":34,"C":35,"D":36,"E":37,"F":38,"G":39,"H":40,"I":41,"J":42,"K":43,"L":44,"M":45,"N":46,"O":47,"P":48,"Q":49,"R":50,"S":51,"T":52,"U":53,"V":54,"W":55,"X":56,"Y":57,"Z":58,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"1":64,"2":65,"3":66,"4":67,"5":68,"6":69,"7":70,"8":71,"9":72,"0":73,"~":74,"!":75,"@":76,"#":77,"$":78,"%":79,"^":80,"&":81,"*":82,"(":83,")":84,"_":85,"-":86,"+":87,"=":88,"{":89,"[":90,"}":91,"]":92,"|":93,"\\":94,":":95,";":96,"\"":97,"'":98,"<":99,",":100,">":101,".":102,"?":103,"/":104,"¯":105,"☒":0," ":105,
    "\x1b[D":128,#lft
    "\x1b[A":129,#up
    "\x1b[C":130,#rght
    "\x1b[B":131,#dwn
    "\x01":132,#bckspace aka ctrl-a
}#repr(input("fish>"))
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
# lda #27
# lxa
# ldav #0
# lya
# pxi
# lda #27
# ldbv #5
# cmp
# jme #25
# ldbv #6
# stb #27
# lda #27
# lxa
# ldav #0
# lya
# pxi
# nop
# hlt
# #5
# """
lines = asembly.split("\n")
if lines[0]!="hlt":
    lines.append("hlt")
stats = {}
lvl2 = []
mac = []
# print(lines)
for line in lines:
    line = line.strip()
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
    mac.append(byt(ops[op]))

    for arg in tokens[1:]:
        lvl2.append(arg)
        if arg in ltrs:
            mac.append(byt(ltrs[arg]))
        elif arg.startswith("'"):
            b=byt(ltrs[arg[1:]])
            mac.append(b)
        elif arg.startswith("#"):
            # if arg[1:]in ltrs:
            #     mac.append(byt(ltrs[arg[1:]]))
            # else:
            b=byt(int(arg[1:]))
            if isinstance(b,list):mac.extend(b)
            else:mac.append(b)
        else:
            mac.append(arg.replace("_", ""))

# Resolve label references
for idx, code in enumerate(mac):
    if code in stats:
        mac[idx] = byt(stats[code])

print(mac,len(mac))
input()