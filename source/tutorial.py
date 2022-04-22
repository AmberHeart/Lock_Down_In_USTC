#导入模块
import sys
import pygame
import pygame.freetype

class Tutorial:
    def Show(self):
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/教程BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        #设置两张图
        stage = []
        stage.append (pygame.image.load("../res/image/教程0.png").convert())
        stage.append (pygame.image.load("../res/image/教程1.png").convert())
        #创建时钟对象（控制游戏的FPS）

        clock = pygame.time.Clock()

        #教程部分主循环
        cnt = 0
                
        while True:
        #锁60帧
            clock.tick(60)
        #处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            buttons = pygame.mouse.get_pressed()
            if cnt == 2:
                return 
            self.blit(stage[cnt],(0,0))
            if buttons[0] == 1:
                cnt += 1