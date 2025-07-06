import pygame
HYPER=True
wid=800
hei=600
pixelSize=7
scrnHght=int(hei/pixelSize)+pixelSize
scrnWdth=int(wid/pixelSize)+pixelSize
ramSize=256*256
stkSize=24
displayMode="auto"
sliceSize=2**4
sectorSize=2**4
diskSize=2**4
driveSize=1
ltr="✂abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,:;'\"!? +-*=%$#~()<>{}[]|/\\"

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((wid, hei))
font = pygame.font.SysFont("Arial", 48)
def rect(x,y,w,h,col):
    pygame.draw.rect(screen, col, pygame.Rect(x, y, w, h))
def line(x1,y1,x2,y2,col):
    pygame.draw.line(screen, col, (x1,y1), (x2,y2), 1)

ltrs={
    "A":33,"B":34,"C":35,"D":36,"E":37,"F":38,"G":39,"H":40,"I":41,"J":42,"K":43,"L":44,"M":45,"N":46,"O":47,"P":48,"Q":49,"R":50,"S":51,"T":52,"U":53,"V":54,"W":55,"X":56,"Y":57,"Z":58,"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"1":64,"2":65,"3":66,"4":67,"5":68,"6":69,"7":70,"8":71,"9":72,"0":73,"~":74,"!":75,"@":76,"#":77,"$":78,"%":79,"^":80,"&":81,"*":82,"(":83,")":84,"_":85,"-":86,"+":87,"=":88,"{":89,"[":90,"}":91,"]":92,"|":93,"\\":94,":":95,";":96,"\"":97,"'":98,"<":99,",":100,">":101,".":102,"?":103,"/":104,"¯":105,"☒":0," ":105,
    "\k[l":128,#lft
    "\k[u":129,#up
    "\k[r":130,#rght
    "\k[d":131,#dwn
    "\k[bk":132,#bckspace aka ctrl-a
}