import  pygame,briks,time
from pygame import display, event
okno = display.set_mode([750, 820])
spisok_kubika=[]
gggg=[100,200,300,400,500,600]

for did in gggg:
    kub1 = pygame.Rect(0,did, 100, 100)
    kub1.centerx = okno.get_width() / 2
    spisok_kubika.append(kub1)


    print(did)

okno = display.set_mode([750, 820])
# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 
hp_kuba=2
while True :

    pygame.event.get()
    okno.fill([0,0,0])
    # pygame.display.flip()
    # time.sleep(1)
    for did in spisok_kubika:

        briks.kub_poyavis(okno,did, hp_kuba)
        # pygame.display.flip()
        # time.sleep(1)
    pygame.display.flip ()


