#导入模块
from ctypes.wintypes import RGB
from operator import index
from random import randint
import sys
from turtle import towards
import pygame
import math

#pygame初始化

pygame.init()

#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("这是一个标题")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#设置背景

image_background = pygame.image.load("../res/image/map.png").convert()
background_x = 320
background_y = -1280

#初始化移动变量

movement_x = 0
movement_y = 0

#定义实体类

class solid(pygame.sprite.Sprite):
    def __init__(self,filename,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        

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
        self.movement = 0
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
max_speed = 12
min_speed = 6

# 设置字体等参数
font = pygame.font.Font("../res/font/Pixel.ttf",45)
font1 = pygame.font.Font("../res/font/Pixel.ttf",25)

black = (0, 0, 0)
white = (255, 255, 255)

#设置物品参数
#饮料 食物 书 杂项 鱼 水果

item_volume = [1,1,2,3,5,10]

#设置背包

bag_volume = 10
bag_left = 10
bag_item = [0,0,0,0,0,0]

#设置战果

result_item = [0,0,0,0,0,0]

#设置物品栏
items_bag = solid("../res/image/物品栏.png",(640-445/2 , 880))

#设置障碍物和柜子

emptypng = []

blocks = []

shelf = []
for i in range(0,6):
    shelf.append([])

shelf_location = []
for i in range(0,6):
    shelf_location.append([])



shelf_empty = []
for i in range(0,6):
    shelf_empty.append([])

def spawn_shelf(t , filename , location , emptylocation, times):
    shelf[t].append(solid(filename , location))
    shelf_empty[t].append(times)
    shelf_location[t].append(emptylocation)

for i in range(8,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*3-1280-40)))
spawn_shelf(0,"../res/image/wrong.png",(1600+320+20,160*4-1280-80),(1600+320,160*4-1280-160),1)
blocks.append(solid("../res/image/wrong.png" , (1600+320+20,160*7-1280)))
spawn_shelf(1,"../res/image/wrong.png",(1600+320+20,160*8-1280-80),(1600+320,160*8-1280-160),1)               
spawn_shelf(0,"../res/image/wrong.png",(160*19+320-20,160*4-1280-80),(160*19+320,160*4-1280-160),1)
blocks.append(solid("../res/image/wrong.png" , (160*19+320-20,160*7-1280)))
spawn_shelf(1,"../res/image/wrong.png",(160*19+320-20,160*8-1280-80),(160*19+320,160*8-1280-160),1)
for i in range(11,19):
    spawn_shelf(0,"../res/image/wrong.png",(160*i+320,160*4-1280-80),(160*i+320,160*4-1280-160),1)
    
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*7-1280)))

    spawn_shelf(1,"../res/image/wrong.png",(160*i+320,160*8-1280-80),(160*i+320,160*8-1280-160),1)
    
blocks.append(solid("../res/image/wrong.png" , (160*8+320+20,160*11-1280)))
spawn_shelf(3,"../res/image/wrong.png",(160*8+320+20,160*12-1280-80),(160*8+320,160*12-1280-160),1)
blocks.append(solid("../res/image/wrong.png" , (160*17+320-20,160*11-1280)))
spawn_shelf(3,"../res/image/wrong.png",(160*17+320-20,160*12-1280-80),(160*17+320,160*12-1280-160),1)
spawn_shelf(3,"../res/image/bigwrong.png",(160*9+320,160*12-1280-80),(160*9+320,160*12-1280-160),2)
spawn_shelf(3,"../res/image/wrong.png",(160*11+320,160*12-1280-80),(160*11+320,160*12-1280-160),1)
spawn_shelf(3,"../res/image/bigwrong.png",(160*12+320,160*12-1280-80),(160*12+320,160*12-1280-160),2)
spawn_shelf(3,"../res/image/wrong.png",(160*14+320,160*12-1280-80),(160*14+320,160*12-1280-160),1)
spawn_shelf(3,"../res/image/bigwrong.png",(160*15+320,160*12-1280-80),(160*15+320,160*12-1280-160),2)
for i in range(9,17):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*11-1280)))

blocks.append(solid("../res/image/wrong.png" , (160*22+320+20,160*5-1280)))
spawn_shelf(2,"../res/image/wrong.png",(160*22+320+20,160*6-1280-80),(160*22+320,160*6-1280-160),1)
blocks.append(solid("../res/image/wrong.png" , (160*22+320+20,160*9-1280)))
spawn_shelf(2,"../res/image/bigwrong.png",(160*22+320+20,160*10-1280-80),(160*22+320,160*10-1280-160),2)
spawn_shelf(2,"../res/image/wrong.png",(160*25+320,160*6-1280-80),(160*25+320,160*6-1280-160),1)
spawn_shelf(2,"../res/image/bigwrong.png",(160*23+320,160*6-1280-80),(160*23+320,160*6-1280-160),2)
spawn_shelf(2,"../res/image/bigwrong.png",(160*24+320,160*10-1280-80),(160*24+320,160*10-1280-160),2)

for i in range(23,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*5-1280)))
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*9-1280)))

for i in range(4,13):
    blocks.append(solid("../res/image/wrong.png" , (160*26+320+20,160*i-1280)))
    
for i in range(8,19):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*15-1280)))

blocks.append(solid("../res/image/wrong.png" , (160*7+320-20,160*6-1280-40)))
for i in range(4,7):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*6-1280-40)))

for i in range(6,9):
    blocks.append(solid("../res/image/wrong.png" , (480+320-20,160*i-1280)))

blocks.append(solid("../res/image/wrong.png" , (160*4+320,160*13-1280)))
blocks.append(solid("../res/image/wrong.png" , (160*5+320-20,160*13-1280)))

for i in range(20,26):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320+20,160*13-1280)))

spawn_shelf(4,"../res/image/wrong.png",(160*6+320,160*14-1280),(160*6+320,160*14-1280),1)
spawn_shelf(4,"../res/image/wrong.png",(160*7+320-20,160*14-1280),(160*7+320,160*14-1280),1)
spawn_shelf(5,"../res/image/wrong.png",(160*19+320+20,160*14-1280),(160*19+320,160*14-1280),1)
    
for i in range(4,6):
    blocks.append(solid("../res/image/wrong.png" , (160*7+320-20,160*i-1280)))

blocks.append(solid("../res/image/wrong.png" , (160*3+320-20,160*9-1280-80)))
blocks.append(solid("../res/image/wrong.png" , (160*3+320-20,160*12-1280)))
for i in range(0,3):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*9-1280-80)))
for i in range(0,3):
    blocks.append(solid("../res/image/wrong.png" , (160*i+320,160*12-1280)))
    
for i in range(9,13):
    blocks.append(solid("../res/image/wrong.png" , (320-40,160*i-1280)))


#定义碰撞函数

def solid_collide_y(a,m_y,b):
    for i in a:
        i.rect.top += m_y
        if pygame.sprite.collide_rect(b , i):
            i.rect.top -= m_y
            return 0
        i.rect.top -= m_y
    return 1

def solid_collide_x(a,m_x,b):
    for i in a:
        i.rect.left += m_x
        if pygame.sprite.collide_rect(b , i):
            i.rect.left -= m_x
            return 0
        i.rect.left -= m_x
    return 1

def solid_collide_xy(a,m_x,m_y,b):
    for i in a:
        i.rect.left += m_x
        i.rect.top += m_y
        if pygame.sprite.collide_rect(b , i):
            i.rect.left -= m_x
            i.rect.top -= m_y
            return 0
        i.rect.left -= m_x
        i.rect.top -= m_y
    return 1

# 在一个新 Surface 对象上绘制文本
def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#定义移动函数
def solid_move(a , m_x, m_y):
    a.rect.left += m_x
    a.rect.top += m_y
    
def all_move(m_x,m_y):
    for i in blocks:
        solid_move(i,m_x,m_y)
    for i in emptypng:
        solid_move(i,m_x,m_y)
    for j in range(0,6):
        for i in shelf[j]:
            solid_move(i,m_x,m_y)

#创建时钟对象（控制游戏的FPS）

clock = pygame.time.Clock()

#主循环

while True:

#控制时间进程
    time = pygame.time.get_ticks()
#初始化倒计时
    clock_ = int(60 - time/1000)
#锁60帧
    clock.tick(60)

#更新速度

    buyer_speed = (int)(max_speed-(max_speed-min_speed)*(bag_volume-bag_left)/bag_volume)
    
#处理事件
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            movement_x = 0
            movement_y = 0
            buyer.movement = 0
        if pygame.key.get_pressed()[pygame.K_w]:
            movement_y = buyer_speed
            buyer.towards = 4
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_s]:
            movement_y = -buyer_speed
            buyer.towards = 2
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_a]:
            movement_x = buyer_speed
            buyer.towards = 3
            buyer.movement = 1
        if pygame.key.get_pressed()[pygame.K_d]:
            movement_x = -buyer_speed
            buyer.towards = 1
            buyer.movement = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if  96 <= background_x <= 480 and -1376 <= background_y <= -1096:
                    for i in range(0,6):
                        result_item[i] += bag_item[i]
                        bag_item[i] = 0
                        bag_left = bag_volume
                if buyer.towards == 4:
                    for j in range(0,4):
                        cnt = 0
                        flag = 1
                        for i in shelf[j]:
                            i.rect.top += 40
                            if pygame.sprite.collide_rect(buyer , i) and shelf_empty[j][cnt] != 0 and bag_left >= item_volume[j]:
                                i.rect.top -= 40
                                bag_left -= item_volume[j]
                                bag_item[j] += 1
                                if shelf_empty[j][cnt] == 1:
                                    shelf_empty[j][cnt] = 0
                                    emptypng.append(solid("../res/image/空柜子.png" , (shelf_location[j][cnt][0]+(background_x-320),shelf_location[j][cnt][1]+(background_y+1280))))
                                elif shelf_empty[j][cnt] == 2:
                                    shelf_empty[j][cnt] = -1
                                else:
                                    emptypng.append(solid("../res/image/空大柜子.png" , (shelf_location[j][cnt][0]+(background_x-320),shelf_location[j][cnt][1]+(background_y+1280))))
                                '''
                                print(shelf_location[j][cnt])
                                print(i.rect.top)
                                print(i.rect.left)
                                '''
                                flag = 0
                                break            
                            i.rect.top -= 40
                            cnt += 1
                        if flag == 0:
                            break
                if buyer.towards == 2:
                    cnt = 0
                    for i in shelf[4]:
                        i.rect.top -= 40
                        if pygame.sprite.collide_rect(buyer , i) and shelf_empty[4][cnt] != 0 and bag_left >= item_volume[4]:
                            i.rect.top += 40
                            bag_left -= item_volume[4]
                            bag_item[4] += 1
                            if shelf_empty[4][cnt] == 1:
                                shelf_empty[4][cnt] = 0
                                emptypng.append(solid("../res/image/空箱子.png" , (shelf_location[4][cnt][0]+(background_x-320),shelf_location[4][cnt][1]+(background_y+1280))))
                                break
                        i.rect.top += 40
                        cnt += 1
                    cnt = 0
                    for i in shelf[5]:
                        i.rect.top -= 40
                        if pygame.sprite.collide_rect(buyer , i) and shelf_empty[5][cnt] != 0 and bag_left >= item_volume[5]:
                            i.rect.top += 40
                            bag_left -= item_volume[5]
                            bag_item[5] += 1
                            if shelf_empty[5][cnt] == 1:
                                shelf_empty[5][cnt] = 0
                                emptypng.append(solid("../res/image/空箱子.png" , (shelf_location[5][cnt][0]+(background_x-320),shelf_location[5][cnt][1]+(background_y+1280))))
                                break
                        i.rect.top += 40
                        cnt += 1
                if buyer.towards == 1:
                    cnt = 0
                    for i in shelf[5]:
                        i.rect.left -= 40
                        if pygame.sprite.collide_rect(buyer , i) and shelf_empty[5][cnt] != 0 and bag_left >= item_volume[5]:
                            i.rect.left += 40
                            bag_left -= item_volume[5]
                            bag_item[5] += 1
                            if shelf_empty[5][cnt] == 1:
                                shelf_empty[5][cnt] = 0
                                emptypng.append(solid("../res/image/空箱子.png" , (shelf_location[5][cnt][0]+(background_x-320),shelf_location[5][cnt][1]+(background_y+1280))))
                                break
                        i.rect.left += 40
                        cnt += 1
                if buyer.towards == 3:
                    cnt = 0
                    for i in shelf[4]:
                        i.rect.left += 40
                        if pygame.sprite.collide_rect(buyer , i) and shelf_empty[4][cnt] != 0 and bag_left >= item_volume[4]:
                            i.rect.left -= 40
                            bag_left -= item_volume[4]
                            bag_item[4] += 1
                            if shelf_empty[4][cnt] == 1:
                                shelf_empty[4][cnt] = 0
                                emptypng.append(solid("../res/image/空箱子.png" , (shelf_location[4][cnt][0]+(background_x-320),shelf_location[4][cnt][1]+(background_y+1280))))
                                break
                        i.rect.left -= 40
                        cnt += 1
  
#处理上下碰撞

    if (movement_x == 0 and movement_y != 0):
        if (solid_collide_y(blocks,movement_y,buyer) == 1):
            flag = 1
            for i in range(0,6):
                if (solid_collide_y(shelf[i],movement_y,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_y += movement_y
                all_move(0, movement_y)
                        
#处理左右碰撞
    if (movement_y == 0 and movement_x != 0):
        if (solid_collide_x(blocks,movement_x,buyer) == 1):
            flag = 1
            for i in range(0,6):
                if (solid_collide_x(shelf[i],movement_x,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_x += movement_x
                all_move(movement_x, 0)
    
#处理斜碰
    if (movement_y != 0 and movement_x != 0):
        flag = 1
        flag_ud = 1
        m_x1 = (int)(movement_x / math.sqrt(2))
        m_y1 = (int)(movement_y / math.sqrt(2))
        flag = 1
        if (solid_collide_xy(blocks,m_x1,m_y1,buyer) == 1):
            for i in range(0,6):
                if (solid_collide_xy(shelf[i],m_x1,m_y1,buyer) == 0):
                    flag = 0
                    break
            if flag == 1:
                background_x += m_x1
                background_y += m_y1
                all_move(m_x1, m_y1)
        else:
            flag = 0
        if flag == 0:
            #处理上下碰撞
            if (solid_collide_y(blocks,movement_y,buyer) == 1):
                flagud = 1
                for i in range(0,6):
                    if (solid_collide_y(shelf[i],movement_y,buyer) == 0):
                        flagud = 0
                        break
                if flagud == 1:
                    background_y += movement_y
                    all_move(0, movement_y)
            #处理左右碰撞
            if (solid_collide_x(blocks,movement_x,buyer) == 1):
                flaglr = 1
                for i in range(0,6):
                    if (solid_collide_x(shelf[i],movement_x,buyer) == 0):
                        flaglr = 0
                        break
                if flaglr == 1:
                    background_x += movement_x
                    all_move(movement_x, 0)
            
#打印图像

    main_screen.blit( image_background , ( background_x , background_y ))

    '''
    for i in blocks:
        main_screen.blit( i.image , i.rect )
    
      
    for j in range(0,6):
        for i in shelf[j]:
            main_screen.blit( i.image , i.rect )
    '''

    for i in emptypng:
        main_screen.blit( i.image , i.rect )
    
    if buyer.movement == 1:
        buyer.update(pygame.time.get_ticks())
    else:
        buyer.index = buyer.firstframe[buyer.towards]
    buyer.image = buyer.images[buyer.index]
    main_screen.blit( buyer.image , buyer.rect )

#绘制倒计时
    clock_g = "距离封校隔离还有"+str(clock_)+"s"
    TextSurf, TextRect = text_objects(clock_g, font, (255,0,0))
    TextRect.center = (640, 75)
    main_screen.blit(TextSurf, TextRect)
#绘制物品数量
    main_screen.blit(items_bag.image,items_bag.rect)
    x = 1
    for x in range(len(bag_item)):
        TextSurf, TextRect = text_objects(str(bag_item[x]), font1, white)
        TextRect.center = (640-160 + x * (430 / 6), 940)
        main_screen.blit(TextSurf, TextRect)
    TextSurf, TextRect = text_objects('背包剩余容量：'+str(bag_left)+'/10', font1, (255,0,0))
    TextRect.center = (640, 850)
    main_screen.blit(TextSurf, TextRect)
    pygame.display.flip()
