import  pygame,briks,time
from pygame import display, event
okno = display.set_mode([700, 800])
fon = pygame.image.load("fon.jpeg")

spisok_kubika=[]
y2=[100,200,300,400,500,600]
x2=[150,250,350,450]
0
for x1 in x2:


    for y1 in y2:
        kub1 = pygame.Rect(x1,y1, 100, 100)
        spisok_kubika.append(kub1)





# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 
hp_kuba=2
while True :

    pygame.event.get()
    okno.fill([0,0,0])
    okno.blit(fon, [0, 0])

    # pygame.display.flip()
    # time.sleep(1)
    for did in spisok_kubika:

        briks.kub_poyavis(okno,did, hp_kuba)
        # pygame.display.flip()
        # time.sleep(1)
    pygame.display.flip ()


