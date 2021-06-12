import  pygame,briks,time,random
from pygame import display, event
okno = display.set_mode([700, 800])
fon = pygame.image.load("fon.jpeg")

spisok_kubika=[]
y2=[100,200,300,400,500,600]
x2=[150,250,350,450]


for x1 in x2:


    for y1 in y2:
        kub1 = pygame.Rect(x1,y1, 100, 100)
        foto = random.randint(1, 100)
        kub0={"rect":kub1,"hp":foto}
        spisok_kubika.append(kub0)





# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 

while True :

    pygame.event.get()
    okno.fill([0,0,0])
    okno.blit(fon, [0, 0])

    # pygame.display.flip()
    # time.sleep(1)
    for did in spisok_kubika:

        briks.kub_poyavis(okno,did)
        # pygame.display.flip()
        # time.sleep(1)
    pygame.display.flip ()


