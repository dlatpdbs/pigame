import pygame as p

p.init()


w=(255,255,255)
v=(255,0,255)

s=[400,400]
i=p.image.load("4.png")
s2=p.display.set_mode(s)
x=100
y=100
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
                        y=y-2
            if event.type==p.KEYUP:
                  if event.key ==p.K_UP:
                        s2.blit(i,(x,y))

                        
            if event.type==p.KEYDOWN:
                  if event.key ==p.K_DOWN:
                        y=y+2
            if event.type==p.KEYUP:
                  if event.key ==p.K_DOWN:
                        s2.blit(i,(x,y))

            if event.type==p.KEYDOWN:
                  if event.key ==p.K_RIGHT:
                        x=x+2
            if event.type==p.KEYUP:
                  if event.key ==p.K_RIGHT:
                        s2.blit(i,(x,y))


            if event.type==p.KEYDOWN:
                  if event.key ==p.K_LEFT:
                        x=x-2
            if event.type==p.KEYUP:
                  if event.key ==p.K_LEFT:
                        s2.blit(i,(x,y))

            if event.type==p.KEYDOWN:
                  if event.key ==p.K_a:
                        w=(255,0,255)

                       
                  

      s2.fill(w)
      s2.blit(i,(x,y))#이미지 위치

      p.display.flip()
      
      
