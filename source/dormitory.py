#导入模块
import sys
import pygame
import random
import pygame.freetype
import os
from eventlist import EventList
from pause import GamePause
from randomdraw import Randdraw

class Dormitory:
    
    def Game2(self,start_item,save):
        #设置背景

        bg = pygame.image.load("../res/image/dormitory.png").convert()
        
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        #文本打印函数
        font1 = pygame.freetype.Font("../res/font/Pixel.ttf",30)
        font1.antialiased = False
        #space_limit = (左,右,上,下)
        def word_print(space_limit ,text, font, color=(255, 255, 255)):
            font.origin = True
            #words = text.split()
            l_left = space_limit[0]
            l_right = space_limit[1]
            l_up = space_limit[2]
            l_down = space_limit[3]
            line_spacing = font.get_sized_height() + 2
            x, y = l_left, line_spacing + l_up
            space = font.get_rect(' ')
            for word in text:
                bounds = font.get_rect(word)
                if x + bounds.width + bounds.x >= l_right:
                    x, y = l_left, y + line_spacing
                font.render_to(self, (x, y), None, color)
                x += bounds.width + space.width
        
        #按钮类
        
        class button(pygame.sprite.Sprite): # ! 两个图像的按钮 初始化条件如下↓
            button_image = []
            on_button_flag = 0
            def __init__(self,filename1,filename2,location,sound_chosen,sound_pressed):
                pygame.sprite.Sprite.__init__(self)
                self.button_image.append(pygame.image.load(filename1))
                self.button_image.append(pygame.image.load(filename2))
                self.image = self.button_image[0]
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.button_chosen_sound = pygame.mixer.Sound(sound_chosen)
                self.button_chosen_sound.set_volume(0.4)
                self.button_pressed_sound = pygame.mixer.Sound(sound_pressed)
                self.button_pressed_sound.set_volume(0.4)
            def update(self):
                pos = pygame.mouse.get_pos()
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                if pos[0] > lpos and pos[0] < rpos and pos[1] > upos and pos[1] < dpos:
                    if self.on_button_flag == 0:
                        self.button_chosen_sound.play()
                        self.on_button_flag = 1
                    self.image = self.button_image[1]
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0]:
                        self.button_pressed_sound.play()
                        return 1
                    else:
                        return 0
                else:
                    self.on_button_flag = 0
                    self.image = self.button_image[0]

        class choice_button(pygame.sprite.Sprite): # !反馈是字体变白的按钮
            def __init__(self,filename1,location,font,text):
                pygame.sprite.Sprite.__init__(self)
                self.image = (pygame.image.load(filename1))
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.text = text
                self.font = font
                self.color = (0,0,0)
            def update(self):
                pos = pygame.mouse.get_pos()
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                if pos[0] > lpos and pos[0] < rpos and pos[1] > upos and pos[1] < dpos:
                    if self.color == (0,0,0):
                        self.color = (255,255,255)
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0]:
                        return 1
                    else:
                        return 0
                else:
                    self.color = (0,0,0)
            def print(self,screen):
                screen.blit(self.image, self.rect)
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                word_print((lpos +20,rpos - 20 , upos +10 , dpos -10), self.text , self.font ,self.color)
                    
                
        #玩家类
        
        class stu: #!人物的各项数值
            def __init__(self, hungry, thirsty, san, clean, gpa):
                #饥饿值
                self.hungry = hungry
                #口渴值
                self.thirsty = thirsty
                #san值
                self.san = san
                #清洁值
                self.clean = clean
                #GPA
                self.gpa = gpa

        #事件类
        class choose_event:
            
            def __init__(self, screen ,filename2 , font, text1, choice_num, texts , resulttexts):
                self.screen = screen
                self.bg_image = pygame.image.load("../res/image/事件.png")
                self.bg_image_topleft = (240, 180)
                self.event_image = pygame.image.load(filename2)
                self.event_image_topleft = (660 , 220)
                self.num = choice_num
                self.font = font
                self.text = text1
                self.choice_text = texts
                self.buttons = []
                self.result_text = resulttexts
                self.chosen = -1
    
                for i in range(0, self.num):
                    self.buttons.append(choice_button("../res/image/选项按钮.png", (840,530+i*75), self.font , self.choice_text[i] ) )

            def update(self):
                #计数器
                cnt = 0
                if self.chosen == -1:
                    for choice_button in self.buttons:
                        if choice_button.update() == 1:
                            self.chosen = cnt    
                        cnt += 1
                
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.screen.blit(self.event_image, self.event_image_topleft)
                word_print((280,620,220,760) , self.text, self.font, (0,0,0))
                if self.chosen == -1:
                    for choice_button in self.buttons:
                        choice_button.print(self.screen)
                else:
                    word_print((690 , 1040 , 530 , 830) , self.result_text[self.chosen], self.font, (0,0,0))
                    
        
        #随机事件

        l_eve_num = 0
        e_eve_num = 0
        r_eve_num = 0
        c_eve_num = 0
        l_no = []
        e_no = []
        r_no = []
        c_no = []
        
        def spawn_event():
            judge_num = random.randint(0,99)
            if 95 <= judge_num:
                #legendary
                a =1
            elif 80 <= judge_num:
                #epic
                a=1
            elif 50 <= judge_num:
                #rare
                a=1
            else:
                #common
                a=1
                
        #test        
        #testbutton = button("../res/image/退出游戏0.png","../res/image/退出游戏1.png",(640,585), "../res/sound/button.mp3", "../res/sound/press.wav")

        te = EventList.evelist[0][0]
        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)

        #开始
        
        if start_item[0] == -1:
            #继续游戏
            continu = 1
        else:
            #从第一天开始
            now_item = Randdraw.getdraw(start_item)
            now_state = stu(100,100,100,100,3.0)
            day = 1
            resteve = 1

        #画面组件
        #下一步
        nextmove = choice_button("../res/image/选项按钮.png", (1130, 880), font1 , "下一步" )
        nextday = choice_button("../res/image/选项按钮.png", (1130, 880), font1 , "下一天" )
        
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
                if event.type == pygame.WINDOWFOCUSLOST:
                    if GamePause.pause(self,1) == 1:
                        return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if GamePause.pause(self,2) == 1:
                            return -1
                
        #更新图像
            now_event.update()
            if now_event.chosen != -1:
                if resteve != 1:
                    if nextmove.update() == 1:
                        resteve -= 1
                        #生成新事件 暂时用测试事件代替
                        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                else:
                    if nextday.update() == 1:
                        resteve = 1
                        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                    

        #打印文本
            
        #打印图像
            self.blit(bg , (0,0))
            now_event.print_event()
            if now_event.chosen != -1:
                if resteve != 1:
                    nextmove.print(self)
                else:
                    nextday.print(self)
        #刷新屏幕
            pygame.display.flip()
