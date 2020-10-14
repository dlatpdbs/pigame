import pygame as p

p.init()


w=(255,255,255)
v=(255,0,255)
w2=100
s=[700,300]
i=p.image.load("8 (2).png")
i2=p.image.load("배경.png")
s2=p.display.set_mode(s)
x=0
y=0
p.display.set_caption("심심해서 만듬")

d=True


while d:


      for event in p.event.get():
            if event.type == p.QUIT:
                  d==False
                  p.quit()
                  quit()

            if event.type==p.KEYDOWN:
                  if event.key ==p.K_UP:
                        w2=  1         
            if event.type==p.KEYDOWN:
                  if event.key ==p.K_DOWN:
                        w2= -1
            if event.type==p.KEYUP:
                  if event.key ==p.K_UP or event.key == p.K_DOWN:
                        w2 = 0

      y += w2            
      s2.fill(w)
      s2.blit(i,(x,y))#이미지 위치
      s2.blit(i2,(0,0))
      p.display.flip()
      
      
