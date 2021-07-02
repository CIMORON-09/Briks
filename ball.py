import  pygame,mayn
ball=pygame.Rect(300,750,45,45)
def risovanie_ball():
    pygame.draw.rect(mayn.fon,[200,100,200],ball)
    pygame.display.flip()
