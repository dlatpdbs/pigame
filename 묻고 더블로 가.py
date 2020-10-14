import pygame as p

p.init()#초기화

s=(800,400)

white=(255,255,255)

sc=p.display.set_mode(s)#해상도(가로,세로)

p.display.set_caption("선생님의 도박 욕구")

b=p.image.load("100.png")
bre=b.get_rect(left=650,top=50)

c=p.image.load("1000.png")
cre=c.get_rect(left=650,top=165)

m=p.image.load("10000.png")
mre=m.get_rect(left=650,top=250)

re=p.image.load("r.png")
rere=re.get_rect(left=30,top=300)

bg=p.image.load("도박판.png")
money=10000
font=p.font.SysFont("malgungothic",20)
playing = True

while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing =False
            p.quit()
            quit()
        if event.type==p.MOUSEBUTTONDOWN:
            if bre .collidepoint(event.pos):
                print(".")
            if cre .collidepoint(event.pos):
                print("..")
            if mre .collidepoint(event.pos):
                print("...")
            if rere .collidepoint(event.pos):
                money=money+10000

    sc.fill(white)
    sc.blit(bg,(0,0000000))
    sc.blit(c,(cre))
    sc.blit(m,(mre))
    sc.blit(b,(bre))
    sc.blit(re,(rere))
    
    text=font.render("돈:{}".format(money),True,(0,0,0))
    sc.blit(text,(0,0))
    p.display.flip()
