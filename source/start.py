#导入模块
import sys
import pygame
import math

# 设置字体等参数
black = (0, 0, 0)
white = (255, 255, 255)
def Start(self):
    font = pygame.font.Font("../res/font/Pixel.ttf",45)
    class stage(pygame.sprite.Sprite):
            def __init__(self,filename,location):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(filename)
                self.rect = self.image.get_rect()
                self.rect.center = location
     #创建时钟对象（控制游戏的FPS）

    clock = pygame.time.Clock()
    stage1 = stage("../res/image/游戏标题.png", (640,200))
    stage2 = stage("../res/image/开始游戏0.png", (640,700))
    stage3 = stage("../res/image/开始游戏1.png", (640,580))
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        buttons = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        text0 = "mouse position: " + str(pos)
        if buttons[0]:
            text0 += "  left button pressed"
        elif buttons[1]:
            text0 += "  middle button pressed"
        elif buttons[2]:
            text0 += "  right button pressed"
        self.fill((0,0,0))
        text0_surface = font.render(text0, True, (255, 0, 0))
        self.blit(text0_surface, (10, 50))
        self.blit(stage1.image,stage1.rect)
        self.blit(stage2.image,stage2.rect)
        #self.blit(stage1,stage1.rect)
        pygame.display.flip()