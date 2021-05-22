import  pygame,briks
from pygame import display, event

kub = pygame.Rect(633, 555, 100, 100)
okno = display.set_mode([750, 825])

hp_kuba=2
while True :
    pygame.event.get()
    okno.fill([0,0,0])
    briks.kub_poyavis(okno,kub,hp_kuba)
    pygame.display.flip ()
