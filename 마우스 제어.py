import pygame as p
import random as r

p.init#초기화

s=(800,400)
n=0

white=(255,255,255)

sc=p.display.set_mode(s)#해상도(가로,세로)

p.display.set_caption("선생님의 요구")

cr=p.image.load("코로나.png")
cr_r=cr.get_rect(left=r.randint(0,700),top=r.randint(0,300))

playing = True

c=False

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if event.type == p.MOUSEBUTTONDOWN:
            print(event.pos[0],event.pos[1])
        if event.type == p.MOUSEBUTTONUP:
            print(event.pos[0],event.pos[1])


    


    sc.fill(white)
    sc.blit(cr,cr_r)
    if cr_r.collidepoint(event.pos[0],event.pos[1]):
        cr_r.left = r.randint(0,700)
        cr_r.top = r.randint(0,300)
    p.display.flip()
            
            
    
