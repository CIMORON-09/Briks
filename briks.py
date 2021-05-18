import pygame
pygame.init()
pygame.font.init()
f=pygame.font.get_default_font()
shrift=pygame.font.SysFont(f,50)
def kub_poyavis(okno,kub,hp_kuba):

    pygame.draw.rect(okno, [0,39,255],kub,0,15)
    pygame.draw.rect(okno, [233, 20, 0], kub,5,15)
    hp_kuba = shrift.render(str(hp_kuba), True, [255, 2, 10])
    okno.blit(hp_kuba,[380, 580,20,20])
    # okno.blit(kub,[100,55,173])