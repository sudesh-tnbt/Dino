import pygame as py
import os

py.init()

width = 1100
height = 600
screen = py.display.set_mode((width, height))

duck = [py.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
        py.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

run = [py.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
       py.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

jump = [py.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]

variables = [py.image.load(os.path.join("Assets/Bird", "Bird1.png")),
             py.image.load(os.path.join("Assets/Bird", "Bird2.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoDead.png")),


             py.image.load(os.path.join("Assets/Dino", "DinoStart.png")),
             py.image.load(os.path.join("Assets/Other", "Cloud.png")),
             py.image.load(os.path.join("Assets/Other", "GameOver.png")),
             py.image.load(os.path.join("Assets/Other", "Reset.png")),
             py.image.load(os.path.join("Assets/Other", "Track.png"))]


class Dinosaur:
    x = 80
    y = 310

    def __init__(self):
        self.duck_img = duck
        self.run_img = run
        self.jump_img = jump

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_x = self.x
        self.dino_y = self.y

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[py.KEYUP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[py.KEYDOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[py.KEYDOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_x = self.x
        self.dino_y = self.y
        self.step_index += 1

    def duck(self):
        pass

    def jump(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.dino_x, self.dino_y))


def main():
    run = True
    clock = py.time.Clock()
    player = Dinosaur()

    while run:
        for event in py.event.get():
            if event.type == py.quit():
                run = False

        screen.fill((255, 255, 255))
        prompt = py.key.get_pressed()

        player.draw(screen)
        player.update(prompt)

    py.quit()


main()