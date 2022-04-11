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

        bg = pygame.image.load("../res/image/寝室.png").convert()
        
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        #文本打印函数
        eventfont = pygame.freetype.Font("../res/font/Pixel.ttf",15)
        eventfont.antialiased = False
        statefont = pygame.freetype.Font("../res/font/Pixel.ttf",15)
        statefont.antialiased = False
        gpafont = pygame.freetype.Font("../res/font/Pixel.ttf",40)
        gpafont.antialiased = False
        font1 = pygame.freetype.Font("../res/font/Pixel.ttf",30)
        font1.antialiased = False
        font2 = pygame.freetype.Font("../res/font/Pixel.ttf",20)
        font2.antialiased = False
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
        
        class button(pygame.sprite.Sprite):
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

        class choice_button(pygame.sprite.Sprite):
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
                word_print((lpos +10,rpos - 8 , upos -4 , dpos -8), self.text , self.font ,self.color)
                    
                
        #玩家类
        
        class stu:
            def __init__(self, hungry, thirsty, san, iq, clean, gpa):
                #饥饿值
                self.hungry = hungry
                #口渴值
                self.thirsty = thirsty
                #san值
                self.san = san
                #智商
                self.iq = iq
                #清洁值
                self.clean = clean
                #GPA
                self.gpa = gpa

        #事件类
        class choose_event:
            
            def __init__(self, screen ,filename2 , font, text1, choice_num, texts , resulttexts):
                self.screen = screen
                self.bg_image = pygame.image.load("../res/image/事件.png")
                self.bg_image_topleft = (128, 120)
                self.event_image = pygame.image.load(filename2)
                self.event_image_topleft = (660 , 220)
                self.num = choice_num
                self.font = font
                self.text = text1
                self.choice_text = texts
                self.buttons = []
                self.result_text = resulttexts
                self.chosen = -1
                self.close = choice_button("../res/image/关闭.png", (1144,130), font2 , "X" )
    
                for i in range(0, self.num):
                    self.buttons.append(choice_button("../res/image/选项.png", (840,530+i*75), eventfont , self.choice_text[i] ) )

            def update(self):
                #计数器
                cnt = 0
                if self.chosen == -1:
                    for choice_button in self.buttons:
                        if choice_button.update() == 1:
                            self.chosen = cnt    
                        cnt += 1
                if self.close.update() == 1:
                    return 1
                return 0
                
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.screen.blit(self.event_image, self.event_image_topleft)
                self.screen.blit(self.event_image, self.event_image_topleft)
                self.close.print(self.screen)
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

        #属性类
        class state:
            def __init__(self, name , location ,color):
                self.name = name
                self.color = color
                self.location = location
                
            def print(self,screen , num):
                word_print(self.location, self.name , statefont , self.color)
                tmpface = pygame.Surface((20,30),flags=pygame.HWSURFACE)
                tmpface.fill(self.color)
                for i in range(0,num):
                    screen.blit(tmpface , (self.location[0]+60+i*20,self.location[2]))
                tmploca = (self.location[0]+260,self.location[1],self.location[2],self.location[3])
                word_print(tmploca, str(num)+"/10" , statefont , self.color)
                    
        #test        
        #testbutton = button("../res/image/退出游戏0.png","../res/image/退出游戏1.png",(640,585), "../res/sound/button.mp3", "../res/sound/press.wav")
        #背包类
        class bag: #!先用上事件的贴图了
            def __init__(self, screen):
                self.screen = screen
                self.bg_image = pygame.image.load("../res/image/箱子.png")
                self.bg_image_topleft = (128, 120)
                self.chosen = -1
                self.close = choice_button("../res/image/关闭.png", (1144,130), font2 , "X" )
            def update(self):       
                if self.close.update() == 1:
                    return 1
                return 0
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.close.print(self.screen)
                
                
        te = EventList.evelist[0][0]
        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
        now_bag = bag(self)
        #开始
        now_state = stu(10,10,10,2,10,3.0)
        day = 1

        resteve = 1            
        eveshown = 0
        bagshown = 0
        if start_item[0] == -1:
            #继续游戏
            continu = 1
        else:
            now_item = Randdraw.getdraw(start_item)
        #画面组件
        #下一步
        nextmove = choice_button("../res/image/选项.png", (1130, 880), font1 , "下一步" )
        nextday = choice_button("../res/image/选项.png", (1130, 880), font1 , "下一天" )
        openevent = choice_button("../res/image/事件余.png" , (1200 , 50) , font1 , "事件余"+str(resteve))
        openbag = choice_button("../res/image/背包.png" , (1100 , 800) , font1 , "背包")
        state_hungry = state("饥饿值",(10 , 10000 , 200 , 10000) , (205,104,57))
        state_thirsty = state("口渴值",(10 , 10000 , 300 , 10000) , (99,184,255))
        state_san = state("san值",(10 , 10000 , 400 , 10000) , (191,62,255))
        state_iq = state("智商",(10 , 10000 , 500 , 10000) , (0,250,154))
        state_clean = state("清洁值",(10 , 10000 , 600 , 10000) , (255,240,245))
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
            if now_event.update() == 1:
                eveshown = 0
            if now_bag.update() == 1:
                bagshown = 0

            if openevent.update() == 1:
                eveshown = 1
            
            if openbag.update() == 1:
                bagshown = 1
            if now_event.chosen != -1:
                if resteve != 1:
                    if nextmove.update() == 1:
                        resteve -= 1
                        #生成新事件 暂时用测试事件代替
                        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                else:
                    if nextday.update() == 1:
                        day += 1
                        resteve = 1
                        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
            openevent.text = "事件余"+str(resteve)

        #打印文本
            
        #打印图像
            self.blit(bg , (0,0))
            state_hungry.print(self,now_state.hungry)
            state_thirsty.print(self,now_state.thirsty)
            state_san.print(self,now_state.san)
            state_iq.print(self,now_state.iq)
            state_clean.print(self,now_state.clean)
            word_print((10 , 10000 , 700 , 10000), "GPA  "+str(now_state.gpa) , gpafont , (255,0,0))
            openevent.print(self)
            openbag.print(self)
            if bagshown == 1:
                now_bag.print_event()
            if eveshown == 1:
                now_event.print_event()
                if now_event.chosen != -1:
                    if resteve != 1:
                        nextmove.print(self)
                    else:
                        nextday.print(self)
            buttons = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()            
            text0 = "mouse position: " + str(pos)
            text0_surface = font1.render(text0, True, (255, 0, 0))
            self.blit(text0_surface, (10, 50))
        #刷新屏幕
            pygame.display.flip()
