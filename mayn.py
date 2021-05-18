import  pygame,briks
from pygame import display, event

kub = pygame.Rect(333, 555, 100, 100)

hp_kuba=2
while True :
    okno= display.set_mode([750, 825])
    briks.kub_poyavis(okno,kub,hp_kuba)

    pygame.display.flip ()
