#导入模块
import sys
import pygame
class Dormitory:
    def Game2(self):
        
        #创建时钟对象（控制游戏的FPS）

        clock = pygame.time.Clock()

        #宿舍部分主循环
                
        while True:

        #锁60帧
            clock.tick(60)
        #处理事件
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
