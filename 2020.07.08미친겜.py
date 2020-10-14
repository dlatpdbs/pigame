import pygame as p

p.init#초기화

s=(600,800)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("적들아,나와라")
ship=p.image.load("u.png")
ship_le=ship.get_rect(left=250,top=700)
bg=p.image.load("o.png")
b=p.image.load("b.png")
b_lest=[]
x=0
y=0
playing = True

while playing:
    b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
    b_lest.append(b_le)

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key ==p.K_UP:
                y=-3
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
            if event.key ==p.K_DOWN:
                y=3
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
            if event.key ==p.K_RIGHT:
                x=3
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
            if event.key ==p.K_LEFT:
                x=-3
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
            if event.key == p.K_SPACE:
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
            
        if event.type == p.KEYUP:
             if event.key ==p.K_UP:
                y=0
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
             if event.key ==p.K_DOWN:
                y=0
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
             if event.key ==p.K_RIGHT:
                x=0
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
             if event.key ==p.K_LEFT:
                x=0
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
             if event.key == p.K_SPACE:
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
        if event.type ==p.MOUSEBUTTONDOWN:
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
        if event.type ==p.MOUSEBUTTONUP:
                b_le=b.get_rect(left=ship_le.left+20,top=ship_le.top)
                b_lest.append(b_le)
                    
            

    ship_le.top += y
    ship_le.left += x
    sc.fill(white)
    
    
    sc.blit(bg,(0,0))
    for b_le in b_lest:
        sc.blit(b,b_le)
    for b_le in b_lest:
        b_le.top -= 4
        
    sc.blit(ship,ship_le)
    p.display.flip()



    
