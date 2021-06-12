import pygame
pygame.init()
pygame.font.init()
f=pygame.font.get_default_font()
shrift=pygame.font.SysFont("arial",50)
def kub_poyavis(okno,kub):
    fon = pygame.image.load("fon.jpeg")

    pygame.draw.rect(okno, [0,39,255],kub["rect"],0,15)
    pygame.draw.rect(okno, [233, 20, 0], kub["rect"],5,15)
    hp_kuba = shrift.render(str(kub["hp"]), True, [0, 255, 10])



    kpd = pygame.Rect(0,0,hp_kuba.get_width(),hp_kuba.get_height() )
    kpd.center=kub["rect"].center
    okno.blit(hp_kuba,[kpd.x,kpd.y])

    # pygame.draw.rect(okno, [233, 20, 0], kpd,5,15)

    # okno.blit(kub,[100,55,173])
