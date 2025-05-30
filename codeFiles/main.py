# displayMode=manual
var x=1
# x=dist(0,9,0,2)
fill(0,15,15)
# pxl(x,0)
# disp()
rect(6,5,2,4)
def randint(randint_min,randint_max)
    seed=mult(74624,seed)
    seed=add(seed, 6358)
    var randint_temp=0
    randint_temp=sqr(2,16)
    seed=mod(seed,randint_temp)
    return seed
fcd
def mod(mod_a,mod_b)
    var mod_temp=0
    mod_temp=div(mod_a,mod_b)
    mod_temp=mult(mod_b,mod_temp)
    mod_temp=sub(mod_a,mod_temp)
    return mod_temp
fcd
def MSB(MSB_n)
    # var MSB_n2=0
    # MSB_n2=SHR(MSB_n2)
    # MSB_n2=SHL(MSB_n2)
    MSB_n=AND(MSB_n,1)
    return MSB_n
fcd
def mult(mult_a,mult_b)
    # # mult_a*=mult_b
    # # return mult_b
    # # pxl(mult_a,mult_b)
    # #load multiplier
    # #check if low (most right) is 1
    # #a-mulitplicand,b-mulitplier
    # var mult_res=0
    # var mult_msb=0
    # flag mult_flag
    # mult_msb=MSB(mult_a)
    # #if not skip addition
    # if mult_msb==1
    #     #add multiplicand to result
    #     mult_res=add(mult_res,mult_a)
    # ifd
    # #shift multiplicand left,
    # mult_a=SHL(mult_a)
    # #shift multiplier right
    # mult_b=SHR(mult_b)
    # #if multiplier 0, we done, oherwise loop
    # if mult_b!=0
    #     goto mult_flag
    # ifd
    # return mult_res
    var mult_x=0
    var mult_a1=0
    var mult_b1=0
    if mult_a>mult_b
        mult_a1=mult_a
        mult_b1=mult_b
    ifd
    if mult_b>mult_a
        mult_a1=mult_b
        mult_b1=mult_a
    ifd
    for mult_i 0 <mult_b1 +=1
        # shl(mult_x)
        mult_x+=mult_a1
    frd
    # # pxl(mult_x,2)
    return mult_x
fcd
def add(add_a,add_b)
    add_a+=add_b
    return add_a
fcd
def div(div_a,div_b)
    var div_t=0
    while div_a>div_b
        div_a-=div_b
        div_t+=1
    whd
    # pxl(div_t,3)
    return div_t
fcd
def sub(sub_a,sub_b)
    sub_a-=sub_b
    return sub_a
fcd
def sqr(sqr_a,sqr_b)
    var sqr_x=sqr_a
    for i 1 <sqr_b +=1
        sqr_a=mult(sqr_a,sqr_x)
    frd
    pxl(sqr_a,4)
    return sqr_a
fcd
def sub2(sub2_a,sub2_b)
    if sub2_a>sub2_b
        sub2_a-=sub2_b
        return sub2_a
    ifd
    sub2_b-=sub2_a
    return sub2_b
fcd
def root(root_num,root_factor)
    var root_guess=0
    var root_guessPow=0
    root_guess=div(root_num,2)
    root_guessPow=sqr(root_guess,2)
    while root_guessPow>root_num
        root_guess-=1
        root_guessPow=sqr(root_guess,2)
        pxl(root_guess,2)
    whd
    return root_guess
fcd
def dist(dist_x1,dist_y1,dist_x2,dist_y2)
    dist_x1=sqr(sub2(dist_x1,dist_x2),2)
    dist_y1=sqr(sub2(dist_y1,dist_y2),2)
    # dist_x2=sqr(dist_x2,2)
    var dist_add=0
    dist_add=add(dist_x1,dist_y1)
    dist_add=root(dist_add,2)
    return dist_add
fcd
# def dist2(dist2_1,dist2_2)
#     var dist2_add=0
#     dist2_add=sub2(dist2_1,dist2_2)
#     return dist2_add
# fcd
def fill(fill_red,fill_green,fill_blue) 
    var fill_temp=0
    # fill_red=div(fill_red,17)
    # fill_green=div(fill_green,17)
    # fill_blue=div(fill_green,17)
    COLOUR=fill_blue
    fill_temp=mult(fill_green,16)
    COLOUR=add(COLOUR,fill_temp)
    fill_temp=mult(fill_red,256)
    # fill_temp=mult(fill_temp,16)
    COLOUR=add(COLOUR,fill_temp)
fcd
def rect(rect_x,rect_y,rect_w,rect_h)
    var rect_x2=0
    rect_x2=add(rect_x,rect_w)
    var rect_y2=0
    rect_y2=add(rect_y,rect_h)
    for rect_iy rect_y <=rect_y2 +=1
        for rect_ix rect_x <=rect_x2 +=1
            pxl(rect_ix,rect_iy)
        ifd
    ifd
    disp()
fcd
def ellipse(ellipse_x,ellipse_y,ellipse_r)
    var ellipse_d=0
    # ellipse_r=div(ellipse_r,2)
    # pxl(ellipse_r,0)
    # pxl(ellipse_x,8)
    # pxl(ellipse_y,9)
    var ellipse_x2=ellipse_x
    ellipse_x2+=mult(ellipse_r,2)#add(ellipse_x,ellipse_r)
    var ellipse_y2=ellipse_y
    ellipse_y2+=mult(ellipse_r,2)
    # pxl(ellipse_x2,12)
    # pxl(ellipse_y2,13)
    var ellipse_cx=ellipse_x
    var ellipse_cy=ellipse_y
    ellipse_x=0
    ellipse_y=0
    for ellipse_iy ellipse_y <=ellipse_y2 +=1
        for ellipse_ix ellipse_x <=ellipse_x2 +=1
            var ellipse_dist=0
            ellipse_dist=dist(ellipse_r,ellipse_r,ellipse_iy,ellipse_ix)
            pxl(ellipse_dist,0)
            if ellipse_dist<=ellipse_r
                var ellipse_tx=ellipse_ix
                ellipse_tx+=ellipse_cx
                var ellipse_ty=ellipse_iy
                ellipse_ty+=ellipse_cy
                pxl(ellipse_tx,ellipse_ty)
            ifd
        frd
    frd
    disp()
fcd