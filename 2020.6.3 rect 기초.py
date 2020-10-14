import pygame as p

p.init()

b=(0,0,0)
w=(255,255,255)
pl = p.image.load("8 (3).png")
#이미지->좌표화
pl_r=pl.get_rect()
bg = p.image.load("배경.png")
e_r=pl.get_rect()
bg_r=pl.get_rect()
e = p.image.load("총알.png")
s=[700,400]
print(pl_r.left)#left=x,top=y
s2=p.display.set_mode(s)

p.display.set_caption("겜판")

dx=0
dy=0

d=False
c=p.time.Clock()

while not d:

      c.tick(10)

      for event in p.event.get():
            if event.type == p.QUIT:
                  d=True

                  
            if event.type == p.KEYDOWN: #키보드를 눌렀을때 반응
                  if event.key == p.K_UP: #위 방향키를 누르면 
                        dy = -2
                  if event.key == p.K_DOWN: 
                        dy = 2
                  if event.key == p.K_RIGHT: 
                        dx = 2
                  if event.key == p.K_LEFT: 
                        dx = -2
            if event.type == p.KEYUP: #키보드를 때었을때 반응
                  if event.key == K_UP or event.key == K_DOWN:
                        dy = 0
                  if event.key == K_RIGHT or event.key == K_LEFT:
                        dx = 0

            pl_r.left +=dx
            pl_r.left +=dy
           
      s2.fill(w)
      s2.blit(pl,pl_r)
      s2.blit(bg,(0,0))
      s2.blit(e,(300,100))
      p.display.flip()
