import pygame
SCREEN_SIZE = 15*32
poz_x = 32
poz_y = 32
poz_k = [[64,64],[64,128],[64,160],[64,192],[64,224],[64,288],[64,320],[64,352],[64,416],
         [96,64],[96,224],[96,416],
         [128,64],[128,160],[128,224],[128,256],[128,320],[128,384],[128,416],
         [192,64],[197,96],[192,160],[192,416],
         [256,64],[265,96],[265,160],[256,416],
         [320,64],[320,96],[320,160],[320,224],[320,256],[320,320],[320,384],[320,416],
         [352,64],[352,224],[352,384],[354,416],
         [384,64],[384,128],[384,160],[384,192],[384,224],[384,288],[384,320],[384,352],[384,416]]

poz_r = [[288,64],[416,416]]
ruch = 0

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

graphics = pygame.image.load("ClassicRPG_Sheet.png")
graphics = pygame.transform.scale(graphics, (320*2, 128*2))

board = [["M","M","M","M","M","M","M","M","M","M","M","M","M","M","M"], #1
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #2
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #3
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #4
         ["M","T","T","T","T","T","T","T","T","T","T","T","K","T","M"], #5
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #6
         ["M","T","T","T","T","T","T","S","S","T","T","T","T","T","M"], #7
         ["M","T","T","T","K","T","T","S","S","T","K","K","K","T","M"], #8
         ["M","T","T","T","T","T","T","S","S","T","T","T","T","T","M"], #9
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #10
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #11
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #12
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #13
         ["M","T","T","T","T","T","T","T","T","T","T","T","T","T","M"], #14
         ["M","M","M","M","M","M","M","M","M","M","M","M","M","M","M"]] #15

dic = {"T":(5*32,2*32,32,32), "D":(4*32,4*32,32,32), "M":(17*31,0*32,32,32), "K":(9*32,5*32,32,32), "S":(14*32,0*32,32,32), "L":(3*32,2*32,32,32), "R":(10*32,6*32,32,32)}


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_RIGHT:
                poz_x = poz_x + 32
            if event.key == pygame.K_LEFT:
                poz_x = poz_x - 32
            if event.key == pygame.K_UP:
                poz_y = poz_y - 32
            if event.key == pygame.K_DOWN:
                poz_y = poz_y + 32

    for i in range(15):
        for j in range(15):
            gameDisplay.blit(graphics,(i*32,j*32), dic["T"])
            gameDisplay.blit(graphics,(i*32,j*32), dic[board[i][j]])

    ludzik = gameDisplay.blit(graphics,(poz_x, poz_y), dic["L"])

    if poz_x>=416:
        poz_x = 416
    if poz_x<=32:
        poz_x = 32
    if poz_y>=416:
        poz_y = 416
    if poz_y<=32:
        poz_y = 32

    for i in range(len(poz_k)):
        skala =  gameDisplay.blit(graphics,(poz_k[i][0], poz_k[i][1]), dic["K"])
        if ludzik.colliderect(skala):
            poz_x = 32
            poz_y = 32

    for i in range(len(poz_r)):
        roslina = gameDisplay.blit(graphics,(poz_r[i][0], poz_r[i][1]), dic["R"])
        if ludzik.colliderect(roslina):
            poz_r[i][0] = 500
            poz_r[i][1] = 500
    pygame.display.update()
