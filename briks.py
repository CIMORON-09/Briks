import pygame,random
pygame.init()
pygame.font.init()
f=pygame.font.get_default_font()
shrift=pygame.font.SysFont("arial",50)
spisok_kubika=[]
def  kub_poyavis(okno,kub):


    pygame.draw.rect(okno, [0,39,255],kub["rect"],0,15)
    pygame.draw.rect(okno, [233, 20, 0], kub["rect"],5,15)
    hp_kuba = shrift.render(str(kub["hp"]), True, [0, 255, 10])



    kpd = pygame.Rect(0,0,hp_kuba.get_width(),hp_kuba.get_height() )
    kpd.center=kub["rect"].center
    okno.blit(hp_kuba,[kpd.x,kpd.y])

    # pygame.draw.rect(okno, [233, 20, 0], kpd,5,15)

    # okno.blit(kub,[100,55,173])
y2 = [100, 200, 300, 400, 500, 600]
x2 = [150, 250, 350, 450]

for x1 in x2:

    for y1 in y2:
        crisnal = random.randint(1, 5)

        kub1 = pygame.Rect(x1, y1, 100, 100)
        kub0 = {"rect": kub1, "hp": crisnal}
        spisok_kubika.append(kub0)

