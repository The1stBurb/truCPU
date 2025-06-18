import pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
img=pygame.image.load("imgs/CrimsonTreeOS.jpg")
running = True
rgb=[]
bitSize=16
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((30, 30, 30))  # Dark gray background

    # Blit (draw) the image at position (x, y)
    screen.blit(img, (0, 0))
    if not rgb:
        for i in range(0,513,16):
            rgb.append([])
            for j in range(0,513,16):
                # print(j,i)
                if i<512 and j<512:
                    rgb[-1].append(img.get_at((j,i)))
    for i in range(0,513,16):
        pygame.draw.line(screen, (0,0,0), (i,0), (i,600), 2)


    # Update the display
    pygame.display.flip()

# Quit Pygame
print(rgb)
def bin_hex(bin_str):
    if len(bin_str)<bitSize:bin_str=bin_str+("0"*(bitSize-len(bin_str)))
    if len(bin_str) != bitSize or any(c not in '01' for c in bin_str):
        raise ValueError("Input must be a 16-character string of '0's and '1's.")
    return hex(int(bin_str, 2))[2:].zfill(4)
def byt(n,lon=False):
    if n<0:
        return "0"*bitSize
    s=""
    for i in range(bitSize-1,-1,-1):
        if 2**i<=n:
            s+="1"
            n-=2**i
        else:
            s+="0"

    return bin_hex(s)
with open("codeFiles/CrimsonTreeOS.img","w")as ctos:
    s=byt(len(rgb[0]))+byt(len(rgb))
    for i in rgb:
        for j in i:
            s+=byt(round(j[0]/10.2)*256+round(j[1]/10.2)*16+round(j[0]/10.2))
    ctos.write(s)
pygame.quit()
quit()