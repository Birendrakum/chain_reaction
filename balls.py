class Player1:
    def __init__(self, state, x, y, in1, in2, in3):
        self.state = state
        self.initial1 = in1
        self.initial2 = in2
        self.initial3 = in3
        self.x = x
        self.y = y
    def update(self, state):
        if state == 1:
            self.initial1 = self.initial1 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))
        elif state == 2:
            self.initial2 = self.initial2 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))
        elif state == 3:
            self.initial3 = self.initial3 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))

class Player2:
    def __init__(self, state, x, y, in1, in2, in3):
        self.state = state
        self.initial1 = in1
        self.initial2 = in2
        self.initial3 = in3
        self.x = x
        self.y = y
    def update(self, state):
        if state == 1:
            self.initial1 = self.initial1 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))
        elif state == 2:
            self.initial2 = self.initial2 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))
        elif state == 3:
            self.initial3 = self.initial3 % 275
            path = "blueball/magic ball (black screen) (5-10-2021 11-11-51 PM)/"
            images = os.listdir(path)
            imagepath = os.path.join(path, images[self.initial1])
            img = pygame.image.load(imagepath)
            img = pygame.transform.scale(img, (60, 35))
            posx = self.x - 70
            posy = self.y - 70
            screen.blit(img, (posx - 70 + 5, posy - 70 + 15))