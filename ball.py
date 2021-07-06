import  pygame
x=300
y=750

ball=pygame.Rect(x,y,45,45)
def risovanie_ball(okno):
        pygame.draw.circle(okno,[200,100,200],[x,y],15,)

def slezhu_za_granicami():
    if ball.y > 800:
        ball.y = -1

    if ball.y < 0:
        ball.y =+1

    if ball.right > 0:
        ball.right =-1


    if ball.x < 700:
        ball.x =-1
# 😁😁😁😆😁😊🍎😳😳🤬🤬🥸🥸