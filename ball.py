import  pygame
x=10
y=300
balle = pygame.Rect(x, y,30,30)


def risovanie_ball(okno):
        pygame.draw.circle(okno,[250,250,250],[balle.x,balle.y],15)


def slezhu_za_granicami():

    if balle.x>685:
        balle.x-=1

# 😁😁😁😆😁😊🍎😳😳🤬🤬🥸🥸