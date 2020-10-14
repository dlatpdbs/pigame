import pygame as p
import random as r
p.init#초기화

s=(800,400)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님의 요구")
playing = True

do=p.image.load("q.png")
do_l=[]
for x in range(20):
    do_r= do.get_rect(left=r.randint(0,720), top=r.randint(0,350))#left=x,top=y
    do_l.append(do_r)
    
    

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if event.type ==p.MOUSEBUTTONDOWN:
            for do_r in do_l:
                if do_r.collidepoint(event.pos[0],event.pos[1]):
                    do_l.remove(do_r)
                    do_r= do.get_rect(left=r.randint(0,720), top=r.randint(0,350))#left=x,top=y
                    do_l.append(do_r)
                


    sc.fill(white)
    for do_r in do_l:
        sc.blit(do,do_r)
        
    p.display.flip()
    
            
            
    
