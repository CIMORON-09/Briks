import pygame

def obrabotk_sobity():
    spisok=pygame.event.get()
    # werty=len(spisok)
    for did in spisok:
        if did.type==pygame.MOUSEBUTTONDOWN:
            print(did.pos[0],did.pos[1])
    # if werty!=0:
    #     # print(spisok)
    #     print(spisok[0])

    # for did in werty:
    #     if did.type == pygame.MOUSEBUTTONDOWN:
    #         print("нажал")