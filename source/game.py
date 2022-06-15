import pygame
import sys
import pygame.freetype
import os
from supermarket import Supermarket
from start import Start
from tutorial import Tutorial
from dormitory import Dormitory
from pause import GamePause
from ending import Ending

#def Game(self):
#pygame 初始化
pygame.init()
                    
#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("LOCK-DOWN IN USTC")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#参数
ending = -1

#游戏循环
while True:
    #GamePause.pause(main_screen)
    startchosen = Start.Game0(main_screen)
    t1 = pygame.time.wait(100)
    if startchosen == 0:
        result = Supermarket.Game1(main_screen)
        if result[0] == -1:
            continue
        t1 = pygame.time.wait(100)
        ending = Dormitory.Game2(main_screen,result,"new_begin")
    elif startchosen == 1:
        Tutorial.Show(main_screen)
        continue
    else:
        with open('save1.txt', 'r') as f:
            save1 = f.read()
        result = [-1]
        ending = Dormitory.Game2(main_screen,result,save1)
            
    
    t1 = pygame.time.wait(100)
    if ending == -1:
        continue
    else:
        os.remove("save1.txt")
        if Ending.print(main_screen, ending) != -1:
            break

#结束游戏

pygame.quit()
sys.exit()
