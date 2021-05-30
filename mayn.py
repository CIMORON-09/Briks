import  pygame,briks
from pygame import display, event
okno = display.set_mode([750, 820])
spisok_kubika=[]

kub1 = pygame.Rect(0,150, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)

kub1 = pygame.Rect(0,250, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)

kub1 = pygame.Rect(0,350, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)

kub1 = pygame.Rect(0, 450, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)

kub1 = pygame.Rect(0, 550, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)

kub1 = pygame.Rect(0, 650, 100, 100)
kub1.centerx=okno.get_width()/2
spisok_kubika.append(kub1)



okno = display.set_mode([750, 820])
# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 
hp_kuba=2
while True :

    pygame.event.get()
    okno.fill([0,0,0])
    for did in spisok_kubika:

        briks.kub_poyavis(okno,did, hp_kuba)

    pygame.display.flip ()
