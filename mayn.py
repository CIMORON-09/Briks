import pygame, briks, ball, random,controller
from pygame import display

okno = display.set_mode([700, 800])

fon = pygame.image.load("fon.png")
p = fon.get_height() / fon.get_width()
fon = pygame.transform.scale(fon, [700, int(700 * p)])
spisok_kubika = []
y2 = [100, 200, 300, 400, 500, 600]
x2 = [150, 250, 350, 450]

for x1 in x2:

    for y1 in y2:
        crisnal = random.randint(1, 5)

        kub1 = pygame.Rect(x1, y1, 100, 100)
        kub0 = {"rect": kub1, "hp": crisnal}
        spisok_kubika.append(kub0)

# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 

while True:
    controller.obrabotk_sobity()
    okno.fill([0, 0, 0])
    okno.blit(fon, [0, 0])
    ball.balle.x += ball.speedx
    ball.balle.y += ball.speedy

    for did in spisok_kubika:
        briks.kub_poyavis(okno, did)

    ball.risovanie_ball(okno)

    ball.slezhu_za_granicami()
    pygame.display.flip()
