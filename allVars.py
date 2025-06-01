import pygame
scrnHght=70
scrnWdth=70
ramSize=256*256
stkSize=24
displayMode="auto"
sliceSize=2**4
sectorSize=2**4
diskSize=2**4
driveSize=1
pixelSize=5
bitSize=16

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Arial", 48)
def rect(x,y,w,h,col):
    pygame.draw.rect(screen, col, pygame.Rect(x, y, w, h))