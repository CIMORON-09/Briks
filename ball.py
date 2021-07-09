import  pygame

x=200
y=200
balle=pygame.Rect(x, y, 45, 45)
def risovanie_ball(okno):
        pygame.draw.circle(okno,[250,250,250],[x,y],15)


def slezhu_za_granicami():

    if balle.y < 800:
        balle.y -=1

    if balle.y < 0:
        balle.y += 1

    if balle.x < 0:
        balle.x-= 1тут ошипка

    if balle.x > 700:
        balle.x-= 1

# 😁😁😁😆😁😊🍎😳😳🤬🤬🥸🥸