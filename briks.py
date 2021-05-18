import pygame

def kub_poyavis(okno,kub):

    pygame.draw.rect(okno, [0,39,255],kub,0,15)
    pygame.draw.rect(okno, [233, 20, 0], kub,5,15)

    # okno.blit(kub,[100,55,173])