# import modules
import pygame
import os
import math

# initialise pygame
pygame.init()
screen = pygame.display.set_mode((900, 630))

# Loading all images into dictionary

dict1 = {}
st = 0
for img in os.listdir("videos/red1resized/"):
    image = pygame.image.load("videos/red1resized/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict1[st] = image
    st += 1

dict2 = {}
st = 0
for img in os.listdir("videos/red2resize/"):
    image = pygame.image.load("videos/red2resize/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict2[st] = image
    st += 1

dict3 = {}
st = 0
for img in os.listdir("videos/red3resize/"):
    image = pygame.image.load("videos/red3resize/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict3[st] = image
    st += 1

dict4 = {}
st = 0
for img in os.listdir("videos/blue1resize/"):
    image = pygame.image.load("videos/blue1resize/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict4[st] = image
    st += 1
dict5 = {}
st = 0
for img in os.listdir("videos/blue2resize/"):
    image = pygame.image.load("videos/blue2resize/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict5[st] = image
    st += 1
dict6 = {}
st = 0
for img in os.listdir("videos/blue3resize/"):
    image = pygame.image.load("videos/blue3resize/" + img)
    image = pygame.transform.scale(image, (50, 50))
    dict6[st] = image
    st += 1


# This function is called when player pause the the game in middle
def pause():
    loop = True
    while loop:
        play = pygame.image.load("images/esc.jpg")
        screen.blit(play, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos[0], pos[1])
                if 322 <= pos[0] <= 619 and 145 <= pos[1] <= 236:
                    loop = False
                if 322 <= pos[0] <= 619 and 237 <= pos[1] <= 328:
                    mainmenu()
                if 322 <= pos[0] <= 619 and 328 <= pos[1] <= 419:
                    exit()
            if event.type == pygame.QUIT:
                exit()


# This function called when game starts
def startgame():
    # This function tells whether current cell explode or not
    def ifexplode(n):
        if n in corner and records[n][1] >= 2:
            return True
        elif (n[0] in boundaryX and boundaryX[n[0]][0] <= n[1] <= boundaryX[n[0]][1] and records[n][1] >= 3) or \
                (n[1] in boundaryY and boundaryY[n[1]][0] <= n[0] <= boundaryY[n[1]][1] and records[n][1] >= 3):
            return True
        elif records[n][1] >= 4:
            return True
        else:
            return False

    # Checks if any player wins or not till now
    def ifwin():
        player1 = 0
        player2 = 0
        img1 = pygame.image.load("images/player1.jpg")
        img2 = pygame.image.load("images/player2.jpg")
        for i in records:
            if records[i][0] == 1:
                player1 += 1
            elif records[i][0] == 2:
                player2 += 1
        if (player1 >= 56 and player2 == 0) or player1 == 70:
            screen.blit(img1, (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            return True
        elif (player2 >= 56 and player1 == 0) or player2 == 70:
            screen.blit(img2, (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            return True
        else:
            return False

    # this function is called when any cell explode
    def burst(arr, parent):
        newarr = {}
        for i in arr:
            temp = {}
            pos1 = i[0] + 90
            pos2 = i[0] - 90
            pos3 = i[1] + 90
            pos4 = i[1] - 90
            if pos1 <= 900:
                records[(pos1, i[1])][1] += 1
                records[(pos1, i[1])][0] = parent
                temp[(pos1, i[1])] = 0
            if pos2 >= 90:
                records[(pos2, i[1])][1] += 1
                records[(pos2, i[1])][0] = parent
                temp[(pos2, i[1])] = 0
            if pos3 <= 630:
                records[(i[0], pos3)][1] += 1
                records[(i[0], pos3)][0] = parent
                temp[(i[0], pos3)] = 0
            if pos4 >= 90:
                records[(i[0], pos4)][1] += 1
                records[(i[0], pos4)][0] = parent
                temp[(i[0], pos4)] = 0

            img = pygame.image.load("images/Untitled.png")
            img = pygame.transform.scale(img, (80, 80))
            screen.blit(img, (i[0] - 80, i[1] - 80))
            records[i][1] = 0
            for t in temp:
                if ifexplode(t):
                    newarr[t] = 0
                    img = pygame.image.load("images/energy.png")
                    img = pygame.transform.scale(img, (80, 80))
                    screen.blit(img, (t[0] - 80, t[1] - 80))
                else:
                    index1 = math.floor(update.in1) % 52
                    index2 = math.floor(update.in2) % 62
                    index3 = math.floor(update.in3) % 50
                    if records[t][0] == 1:
                        redupdate(records[t][1], t[0], t[1], index1, index2, index3)
                    if records[t][0] == 2:
                        blueupdate(records[t][1], t[0], t[1], index1, index2, index3)
            pygame.display.update()
            pygame.time.delay(100)
        winner = ifwin()
        if winner:
            global key
            key = False
            exit()
        if len(newarr) > 0:
            burst(newarr, parent)

    # check if current cell blit red or not
    def redupdate(state, x, y, initial1, initial2, initial3):
        posx = x - 70
        posy = y - 70
        explode = False
        if state == 1:
            # print("r--1", x, y)
            screen.blit(dict1[initial1], (posx, posy))
        elif state == 2 or ((x, y) in corner and state >= 2):
            # print("r--2")
            if (x, y) in corner:
                explode = True
            else:
                screen.blit(dict2[initial2], (posx, posy))
        elif state == 3 or (x in boundaryX and boundaryX[x][0] <= y <= boundaryX[x][1] and state >= 3) or \
                (y in boundaryY and boundaryY[y][0] <= x <= boundaryY[y][1] and state >= 3):
            # print("r--3")
            if x in boundaryX and boundaryX[x][0] <= y <= boundaryX[x][1]:
                explode = True
            elif y in boundaryY and boundaryY[y][0] <= x <= boundaryY[y][1]:
                explode = True
            else:
                screen.blit(dict3[initial3], (posx, posy))
        elif state >= 4:
            # print("r--4", x, y)
            explode = True
        if explode:
            fade = pygame.Surface((900, 630))
            fade.set_alpha(100)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            burst({(x, y): 0}, 1)
            pygame.time.delay(300)
            displaycustom()
            pygame.display.update()

    # check if current cell blit blue or not
    def blueupdate(state, x, y, initial1, initial2, initial3):
        posx = x - 70
        posy = y - 70
        explode = False
        if state == 1:
            # print(("b--1"))
            screen.blit(dict4[initial1], (posx, posy))
        elif state == 2 or ((x, y) in corner and state >= 2):
            # print("b--2")
            if (x, y) in corner:
                explode = True
            else:
                screen.blit(dict5[initial2], (posx, posy))
        elif state == 3 or (x in boundaryX and boundaryX[x][0] <= y <= boundaryX[x][1] and state >= 3) or \
                (y in boundaryY and boundaryY[y][0] <= x <= boundaryY[y][1] and state >= 3):
            # print("b3")
            if x in boundaryX and boundaryX[x][0] <= y <= boundaryX[x][1]:
                explode = True
            elif y in boundaryY and boundaryY[y][0] <= x <= boundaryY[y][1]:
                explode = True
            else:
                screen.blit(dict6[initial3], (posx, posy))
        elif state >= 4:
            # print("b4")
            explode = True
        if explode:
            fade = pygame.Surface((900, 630))
            fade.set_alpha(100)
            screen.blit(fade, (0, 0))
            pygame.display.update()
            burst({(x, y): 0}, 2)
            pygame.time.delay(300)
            displaycustom()
            pygame.display.update()

    def displaycustom():
        # vertical lines
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 250), (0, 0), (0, 630))
        pygame.draw.line(screen, (255, 255, 250), (90, 0), (90, 630))
        pygame.draw.line(screen, (255, 255, 250), (180, 0), (180, 630))
        pygame.draw.line(screen, (255, 255, 250), (270, 0), (270, 630))
        pygame.draw.line(screen, (255, 255, 250), (360, 0), (360, 630))
        pygame.draw.line(screen, (255, 255, 250), (450, 0), (450, 630))
        pygame.draw.line(screen, (255, 255, 250), (540, 0), (540, 630))
        pygame.draw.line(screen, (255, 255, 250), (630, 0), (630, 630))
        pygame.draw.line(screen, (255, 255, 250), (720, 0), (720, 630))
        pygame.draw.line(screen, (255, 255, 250), (810, 0), (810, 630))
        pygame.draw.line(screen, (255, 255, 250), (899, 0), (899, 630))

        # horizontal lines
        pygame.draw.line(screen, (255, 255, 250), (0, 90), (900, 90))
        pygame.draw.line(screen, (255, 255, 250), (0, 180), (900, 180))
        pygame.draw.line(screen, (255, 255, 250), (0, 270), (900, 270))
        pygame.draw.line(screen, (255, 255, 250), (0, 360), (900, 360))
        pygame.draw.line(screen, (255, 255, 250), (0, 450), (900, 450))
        pygame.draw.line(screen, (255, 255, 250), (0, 540), (900, 540))
        pygame.draw.line(screen, (255, 255, 250), (0, 630), (900, 630))
        pygame.draw.line(screen, (255, 255, 250), (0, 0), (900, 0))
        pygame.draw.line(screen, (255, 255, 250), (0, 629), (900, 629))
        fade = pygame.Surface((900, 630))
        fade.set_alpha(150)
        screen.blit(fade, (0, 0))

    # keep records of each cell
    records = {(90, 90): [0, 0], (180, 90): [0, 0], (270, 90): [0, 0], (360, 90): [0, 0], (450, 90): [0, 0],
               (540, 90): [0, 0], (630, 90): [0, 0], (720, 90): [0, 0], (810, 90): [0, 0], (900, 90): [0, 0],
               (90, 180): [0, 0], (180, 180): [0, 0], (270, 180): [0, 0], (360, 180): [0, 0], (450, 180): [0, 0],
               (540, 180): [0, 0], (630, 180): [0, 0], (720, 180): [0, 0], (810, 180): [0, 0], (900, 180): [0, 0],
               (90, 270): [0, 0], (180, 270): [0, 0], (270, 270): [0, 0], (360, 270): [0, 0], (450, 270): [0, 0],
               (540, 270): [0, 0], (630, 270): [0, 0], (720, 270): [0, 0], (810, 270): [0, 0], (900, 270): [0, 0],
               (90, 360): [0, 0], (180, 360): [0, 0], (270, 360): [0, 0], (360, 360): [0, 0], (450, 360): [0, 0],
               (540, 360): [0, 0], (630, 360): [0, 0], (720, 360): [0, 0], (810, 360): [0, 0], (900, 360): [0, 0],
               (90, 450): [0, 0], (180, 450): [0, 0], (270, 450): [0, 0], (360, 450): [0, 0], (450, 450): [0, 0],
               (540, 450): [0, 0], (630, 450): [0, 0], (720, 450): [0, 0], (810, 450): [0, 0], (900, 450): [0, 0],
               (90, 540): [0, 0], (180, 540): [0, 0], (270, 540): [0, 0], (360, 540): [0, 0], (450, 540): [0, 0],
               (540, 540): [0, 0], (630, 540): [0, 0], (720, 540): [0, 0], (810, 540): [0, 0], (900, 540): [0, 0],
               (90, 630): [0, 0], (180, 630): [0, 0], (270, 630): [0, 0], (360, 630): [0, 0], (450, 630): [0, 0],
               (540, 630): [0, 0], (630, 630): [0, 0], (720, 630): [0, 0], (810, 630): [0, 0], (900, 630): [0, 0]
               }

    # This function check each cell and calls redupdate or blueupdate on current cell
    class Update:
        def __init__(self):
            self.in1 = 0
            self.in2 = 0
            self.in3 = 0

        def update(self):
            self.in1 += 0.2
            self.in2 += 0.4
            self.in3 += 0.8
            index1 = math.floor(self.in1) % 52
            index2 = math.floor(self.in2) % 62
            index3 = math.floor(self.in3) % 50
            for i in records:
                j = records[i]
                if j[0] == 0:
                    pass
                elif j[0] == 1:
                    redupdate(j[1], i[0], i[1], index1, index2, index3)
                else:
                    blueupdate(j[1], i[0], i[1], index1, index2, index3)

    update = Update()
    corner = {(90, 90): 0, (900, 90): 0, (90, 630): 0, (900, 630): 0}
    boundaryX = {90: (180, 540), 900: (180, 540)}
    boundaryY = {90: (180, 810), 630: (180, 810)}
    pygame.display.update()
    key = True
    toogle = 0
    displaycustom()
    while key:
        if toogle == 0:
            pygame.display.set_caption("player 1 turn")
        else:
            pygame.display.set_caption("player 2 turn")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                key = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if toogle == 0:
                    x = 90 - (event.pos[0] % 90) + event.pos[0]
                    y = 90 - (event.pos[1] % 90) + event.pos[1]
                    records[(x, y)][0] = 1
                    records[(x, y)][1] += 1
                    toogle = (toogle + 1) % 2
                elif toogle == 1:
                    x = 90 - (event.pos[0] % 90) + event.pos[0]
                    y = 90 - (event.pos[1] % 90) + event.pos[1]
                    records[(x, y)][0] = 2
                    records[(x, y)][1] += 1
                    toogle = (toogle + 1) % 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause()
                displaycustom()
        update.update()
        pygame.display.update()
        check = ifwin()
        if check:
            key = False
    pygame.quit()


# this function creates main menu
def mainmenu():
    main = True
    while main:
        img = pygame.image.load("images\main.jpg")
        screen.blit(img, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click", pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                pos = pygame.mouse.get_pos()
                if 65 <= pos[0] <= 166 and 123 <= pos[1] <= 150:
                    startgame()
                    main = False
                if 65 <= pos[0] <= 166 and 151 <= pos[1] <= 178:
                    img = pygame.transform.scale(pygame.image.load(r"images\rules.jpeg"), (900, 630))
                    key = True
                    while key:
                        screen.blit(img, (0, 0))
                        pygame.display.update()
                        for events in pygame.event.get():
                            if events.type == pygame.QUIT:
                                key = False
                if 65 <= pos[0] <= 166 and 179 <= pos[1] <= 214:
                    exit()
            if event.type == pygame.QUIT:
                exit()


mainmenu()
