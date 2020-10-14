import pygame as p

p.init#초기화

s=(800,600)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("선생님의 요구")
oto=p.image.load("오토.png")

o_re=oto.get_rect(left=0,top=250)
oy=10
clo=p.time.Clock()
rects=[]
for x in range(80):
    rect=p.Rect(x*10,100,10,400)
    rects.append(rect)
    
    



 
playing = True
black=(0,0,0)

go=False
ex=p.image.load("boom.png")




while playing:
    clo.tick(15)
    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
            
        if event.type==p.KEYDOWN:
            if event.key==p.K_SPACE:
                 oy=-oy
    
    sc.fill(black)
    
    #화면업로드
    for rect in rects:
         p.draw.rect(sc,white,rect)
    sc.blit(oto,o_re)
    for rect in rects:
         rect.left=rect.left-10
    del rects[0]

    






    
    # 비행기가 동굴이랑 충돌하면?
    if o_re.top<rects[0].top or o_re.bottom>rects[0].bottom:
        go=True
    if go:
        ex_re=ex.get_rect(left=o_re.left-20,top=o_re.top-20)
        sc.blit(ex,ex_re)

    o_re.top+=oy
    p.display.flip()
            
            
    
