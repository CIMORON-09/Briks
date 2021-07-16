import pygame

x = 10
y = 300
speedx = 2
speedy = 2
balle = pygame.Rect(x, y, 30, 30)


def risovanie_ball(okno):
    pygame.draw.circle(okno, [250, 250, 250], [balle.centerx, balle.centery], 15)
    # pygame.draw.rect(okno,[2,25,250],balle,5)

def slezhu_za_granicami():
    global speedx, speedy
    if balle.right > 700:
        speedx =-2

    if balle.left < 0:
        speedx = +2
    print(speedx)

    if balle.y < 0:
        speedy =+2

    if balle.bottom >800:
        speedy =-2

# 😁😁😁😆😁😊🍎😳😳🤬🤬🥸🥸
