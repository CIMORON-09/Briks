import  pygame,briks
from pygame import display, event
okno = display.set_mode([750, 820])

kub1 = pygame.Rect(0,150, 100, 100)
kub1.centerx=okno.get_width()/2

kub2 = pygame.Rect(0,250, 100, 100)
kub2.centerx=okno.get_width()/2

kub3 = pygame.Rect(0,350, 100, 100)
kub3.centerx=okno.get_width()/2

kub4 = pygame.Rect(0, 450, 100, 100)
kub4.centerx=okno.get_width()/2

kub5 = pygame.Rect(0, 550, 100, 100)
kub5.centerx=okno.get_width()/2

kub6 = pygame.Rect(0, 650, 100, 100)
kub6.centerx=okno.get_width()/2



okno = display.set_mode([750, 820])
# ДЕНЬ РОЖДЕНИЯ У МОЕГО УЧИТЕЛЯ 4 СЕНТЯБРЯ!!(cool) 
hp_kuba=2
while True :
    pygame.event.get()
    okno.fill([0,0,0])
    briks.kub_poyavis(okno, kub1, hp_kuba)
    briks.kub_poyavis(okno, kub2, hp_kuba)
    briks.kub_poyavis(okno, kub3, hp_kuba)
    briks.kub_poyavis(okno, kub4, hp_kuba)
    briks.kub_poyavis(okno, kub5, hp_kuba)
    briks.kub_poyavis(okno, kub6, hp_kuba)
    pygame.display.flip ()
