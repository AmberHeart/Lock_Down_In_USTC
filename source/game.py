import pygame
import sys
from supermarket import Supermarket
from start import Start
from dormitory import Dormitory

#pygame 初始化
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("../res/sound/BGM.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
                    
#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("这是一个标题")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#开始界面
Start.Game0(main_screen)
result = Supermarket.Game1(main_screen)
#Dormitory.Game2(main_screen)

#结束游戏
pygame.quit()
sys.exit()
