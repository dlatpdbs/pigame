import pygame as p

p.init()

b=(0,0,0)
w=(255,255,255)
b2=(0,0,255)
g=(0,255,0)
r=(255,0,0)
s=[400,300]

s2=p.display.set_mode(s)

p.display.set_caption("겜판")

d=False
c=p.time.Clock()

while not d:

      c.tick(10)

      for event in p.event.get():
            if event.type == p.QUIT:
                  d=True
