import pygame as p

p.init#초기화

s=(800,600)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님의 요구")
oto=p.image.load("오토.png")
o_re=oto.get_rect(left=0,top=250)


playing = True

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()


    sc.fill(white)
    sc.blit(oto,o_re)
    p.display.flip()
            
            
    
