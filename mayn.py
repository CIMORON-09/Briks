import pygame, briks, ball, random,controller
from pygame import display

okno = display.set_mode([700, 800])

fon = pygame.image.load("fon.png")
p = fon.get_height() / fon.get_width()
fon = pygame.transform.scale(fon, [700, int(700 * p)])

# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 

while True:
    controller.obrabotk_sobity()
    okno.fill([0, 0, 0])
    okno.blit(fon, [0, 0])
    ball.balle.x += ball.speedx
    ball.balle.y += ball.speedy

    for did in briks.spisok_kubika:
        briks.kub_poyavis(okno, did)

    ball.risovanie_ball(okno)

    ball.slezhu_za_granicami()
    pygame.display.flip()
