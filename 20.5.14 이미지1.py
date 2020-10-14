import pygame as p

p.init()

s=(2000,1000)
w=(255,255,255)
b=(0,0,255)
r=(255,0,0)
g=(0,255,0)
#e=p.image.load("1.png")
#i=p.image.load("2.png")
c=p.image.load("3.png")
p.mixer.music.load("3.mp3")
sc=p.display.set_mode(s)
p.mixer.music.play(0)
p.display.set_caption("너 이걸보면 오늘 못잠^^")

d=False

while not d:
      for event in p.event.get():
            if event.type ==p.QUIT:
                  d=True




      sc.fill(w)
      #sc.blit(e,(100,150))
      #sc.blit(i,(100,220))
      sc.blit(c,(1000,400))
      p.display.flip()
                 

