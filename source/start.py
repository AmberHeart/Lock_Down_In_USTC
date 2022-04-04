#导入模块
import sys
import pygame
import math
class Start:
    def Game0(self):
        #设置背景

        image_background = pygame.image.load("../res/image/map.png").convert()
        background_x = -900
        background_y = -1000

        #初始化移动变量

        movement_x = 0
        movement_y = 0
        # 定义玩家类


        class player(pygame.sprite.Sprite):
            def __init__(self, filename, frames=1):   # 造型frames默认为1
                pygame.sprite.Sprite.__init__(self)
                self.images = []
                img = pygame.image.load(filename)
                self.original_width = img.get_width() // 3
                self.original_height = img.get_height() // 4        # 分割图片
                x = 0
                y = 0
                for frame_no in range(frames):
                    self.images.append(img.subsurface((x, y, 128, 128)))
                    x += self.original_width
                    if x == 3 * self.original_width:
                        x = 0
                        y += self.original_height
                self.index = 7
                self.image = self.images[self.index]
                self.rect = self.image.get_rect()
                self.rect.topleft = [640-64, 480-64]
                self.last_time = 0
                self.towards = 1
                self.movement = 1
                self.firstframe = {1: 7, 2: 1, 3: 4, 4: 10}
                self.lastframe = {1: 9, 2: 3, 3: 6, 4: 12}

            def update(self, current_time):
                x = self.firstframe[self.towards]
                y = self.lastframe[self.towards]
                if self.index <= x - 1:
                    self.index = x - 1
                if current_time - self.last_time > 150:
                    self.index += 1
                    self.last_time = current_time
                if self.index >= y:
                    self.index = x - 1

        #设置角色
                
        buyer = player("../res/image/人物.png", 12)
        buyer_speed = 12

        #创建时钟对象（控制游戏的FPS）

        clock = pygame.time.Clock()

        #计数器

        cnt = 0

        #开始界面主循环
                
        while True:
            
            cnt += 1
            
        #锁60帧
            clock.tick(60)
      
        #处理事件
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if cnt == 110 or cnt == 140:
                buyer.towards -= 1
                if buyer.towards == 0:
                    buyer.towards = 4
                if cnt == 140:
                    cnt = 0
            if buyer.towards == 1:
                background_x -= 16
            if buyer.towards == 2:
                background_y -= 16
            if buyer.towards == 3:
                background_x += 16
            if buyer.towards == 4:
                background_y += 16
                    
        #打印图像

            self.blit( image_background , ( background_x , background_y ))

            if buyer.movement == 1:
                buyer.update(pygame.time.get_ticks())
            else:
                buyer.index = buyer.firstframe[buyer.towards]
            buyer.image = buyer.images[buyer.index]
            self.blit( buyer.image , buyer.rect )
            
            pygame.display.flip()
