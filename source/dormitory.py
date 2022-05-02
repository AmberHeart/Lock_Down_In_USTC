#导入模块
from subprocess import STARTF_USESTDHANDLES
import sys
import pygame
import random
import pygame.freetype
import os
from supermarket import Supermarket
from eventlist import EventList
from pause import GamePause
from randomdraw import Randdraw

class Dormitory:
    
    def Game2(self,start_item,save):
        
        #设置背景
        message_bg = pygame.image.load("../res/image/状态栏背景.png").convert()
        
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        #文本打印函数
        eventpFont = pygame.font.Font("../res/font/Pixel.ttf",25)
        eventpFont2 = pygame.font.Font("../res/font/Pixel.ttf",15)
        eventpFont3 = pygame.font.Font("../res/font/Pixel.ttf",20)
        eventfont = pygame.freetype.Font("../res/font/Pixel.ttf",20)
        eventfont.antialiased = False
        eventpfont = pygame.freetype.Font("../res/font/Pixel.ttf",25)
        eventpfont.antialiased = False
        statefont = pygame.freetype.Font("../res/font/Pixel.ttf",15)
        statefont.antialiased = False
        gpafont = pygame.freetype.Font("../res/font/Pixel.ttf",40)
        gpafont.antialiased = False
        tipsfont = pygame.freetype.Font("../res/font/Pixel.ttf",50)
        tipsfont.antialiased = False
        timefont = pygame.freetype.Font("../res/font/LCD.TTF",40)
        timefont.antialiased = False
        timefont2 = pygame.freetype.Font("../res/font/LCD.TTF",20)
        timefont2.antialiased = False
        messagefont = pygame.freetype.Font("../res/font/Pixel.ttf",15)
        messagefont.antialiased = False
        font1 = pygame.freetype.Font("../res/font/Pixel.ttf",30)
        font1.antialiased = False
        font2 = pygame.freetype.Font("../res/font/Pixel.ttf",20)
        font2.antialiased = False
        font3 = pygame.freetype.Font("../res/font/Pixel.ttf",20)
        font3.antialiased = False
        
        #testfont
        testfont = pygame.font.Font("../res/font/Pixel.ttf",25)
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
        pressed = [0]
        
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
            def update(self,pressed):
                pos = pygame.mouse.get_pos()
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                if pos[0] > lpos and pos[0] < rpos and pos[1] > upos and pos[1] < dpos:
                    if self.color == (0,0,0):
                        self.color = (255,255,255)
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] and pressed[0] == 1:
                        pressed[0] = 0
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

        def text_objects(text, font,color):
            textSurface = font.render(text, True, color)
            return textSurface, textSurface.get_rect()
                
            #居中按钮
        class choice_button1(pygame.sprite.Sprite):
            def __init__(self,filename1,location,font,text):
                pygame.sprite.Sprite.__init__(self)
                self.image = (pygame.image.load(filename1))
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.text = text
                self.font = font
                self.color = (0,0,0)
            def update(self,pressed):
                pos = pygame.mouse.get_pos()
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                if pos[0] > lpos and pos[0] < rpos and pos[1] > upos and pos[1] < dpos:
                    if self.color == (0,0,0):
                        self.color = (255,255,255)
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] and pressed[0] == 1:
                        pressed[0] = 0
                        return 1
                    else:
                        return 0
                else:
                    self.color = (0,0,0)
            def print(self,screen):
                screen.blit(self.image, self.rect)
                TextSurf, TextRect = text_objects(self.text,self.font,self.color)
                TextRect.center = self.rect.center
                screen.blit(TextSurf, TextRect)
                        
        class choice_button2(pygame.sprite.Sprite):
            def __init__(self,filename1,location,font,text):
                pygame.sprite.Sprite.__init__(self)
                self.image = (pygame.image.load(filename1))
                self.rect = self.image.get_rect()
                self.rect.center = location
                self.text = text
                self.font = font
                self.color = (0,0,0)
            def update(self,pressed):
                pos = pygame.mouse.get_pos()
                lpos = self.rect.center[0] - self.image.get_width()/2
                rpos = self.rect.center[0] + self.image.get_width()/2
                upos = self.rect.center[1] - self.image.get_height()/2
                dpos = self.rect.center[1] + self.image.get_height()/2
                if pos[0] > lpos and pos[0] < rpos and pos[1] > upos and pos[1] < dpos:
                    if self.color == (0,0,0):
                        self.color = (255,0,0)
                    buttons = pygame.mouse.get_pressed()
                    if buttons[0] and pressed[0] == 1:
                        pressed[0] = 0
                        return 1
                    else:
                        return 0
                else:
                    self.color = (0,0,0)
            def print(self,screen):
                screen.blit(self.image, self.rect)
                TextSurf, TextRect = text_objects(self.text,self.font,self.color)
                TextRect.center = self.rect.center
                screen.blit(TextSurf, TextRect)
        #玩家类
        
        class stu:
            #饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) GPA
            def __init__(self, hungry, thirsty, san, iq, clean , day_time , gpa):
                self.state = [hungry,thirsty,san,iq,clean,day_time]
                #GPA
                self.gpa = gpa
                #结局参数
                self.too_low = [0,0,0,0,0]
                self.without_fruit = 0
                self.hesuan = 0
                self.wangwang = [0,0,0,0,0,0] #收集旺旺进度 雪饼，仙贝，牛奶糖，牛奶，挑豆，粟米条
                self.exam = 0
                self.ET = 0
                self.go_out = 0
                self.quality = [0,0,0,0,0] #德智体美劳五个指标
                

            def updatestate(self,consume):

                if consume[0] > 0 and self.without_fruit >= 10:
                    consume[2] -= 1
                for i in range(0,5):
                    self.state[i] += consume[i]
                    if self.state[i] < 0:
                        self.too_low[i] -= self.state[i]
                        student.state[i] = 0
                    elif self.state[i] != 0:
                        self.too_low[i] = 0
                    if self.state[i] > 10:
                        student.state[i] = 10
                student.state[5] += consume[5]
                if student.state[5] >= 96:
                    student.state[5] -= 96

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
                self.close = choice_button("../res/image/关闭.png", (1144,130), font1 , "×" )
                self.tipstime = 0
                self.tipstr = ""
    
                for i in range(0, self.num):
                    self.buttons.append(choice_button("../res/image/选项.png", (840,530+i*75), eventfont , self.choice_text[i] ) )

            def update(self,student,eveid,pressed):
                #计数器
                cnt = 0
                tiptext = ["饥饿值","口渴值","san值","智商","清洁值"]
                if self.chosen == -1:
                    for choice_button in self.buttons:
                        if choice_button.update(pressed) == 1:
                            flag = 0
                            self.tipstr = ""
                            for i in range(0,5):
                                if EventList.limit[eveid][cnt][i] > student.state[i]:
                                    if flag == 0:
                                        flag = 1
                                        self.tipstr = tiptext[i] + self.tipstr
                                    else:
                                        self.tipstr = tiptext[i] + "和" + self.tipstr
                            if flag == 1:
                                self.tipstr = self.tipstr + "不足！！！"
                                self.tipstime = 30
                            else:
                                self.chosen = cnt    
                        cnt += 1
                if self.close.update(pressed) == 1:
                    return 1
                return 0
                
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.screen.blit(self.event_image, self.event_image_topleft)
                self.screen.blit(self.event_image, self.event_image_topleft)
                self.close.print(self.screen)
                word_print((280,620,220,760) , self.text, self.font, (255,255,255))
                if self.chosen == -1:
                    for choice_button in self.buttons:
                        choice_button.print(self.screen)
                else:
                    word_print((690 , 1040 , 530 , 830) , self.result_text[self.chosen], self.font, (255,255,255))
                    
        
        #随机事件
        
        def Check(eveid, state):
            if eveid == 10:
                if student.wangwang[0] == 0 or student.wangwang[1] == 0 or student.wangwang[3] == 0 or student.wangwang[4] == 0 or student.wangwang[5] == 0:
                    return 0
            for i in range(0,5):
                if EventList.refreshneed[eveid][i] > state[i]:
                    return 0
            if EventList.refreshneed[eveid][5] == 0 and EventList.refreshneed[eveid][6] == 0:
                return 1
            if EventList.refreshneed[eveid][5] <= state[5] and state[5] <= EventList.refreshneed[eveid][6]:
                return 1
            else:
                return 0
        def spawn_event(state):
            judge_num = random.randint(0,EventList.event_num - 1)
            while Check(judge_num, state) == 0:
                judge_num = random.randint(0,EventList.event_num - 1)
            return EventList.evelist[judge_num] , judge_num

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

        #背包类
        class bag: 
            def __init__(self, screen, items):
                self.screen = screen
                self.bg_image = pygame.image.load("../res/image/箱子.png")
                self.bg_image_topleft = (128, 120)
                self.chosen = -1
                self.close = choice_button("../res/image/关闭.png", (1144,130), font1 , "×" )
                self.itemnum = items
                self.item =[[],[],[],[]]
                itemlevel=["传奇","稀有","优秀","普通"]
                for y in range(0,4):
                    self.item[0].append(choice_button("../res/image/背包选项.png", (973,283+y*40),font3, itemlevel[y] +"物品剩余数量"+str(self.itemnum[0][y])))
                for y in range(0,4):
                    self.item[1].append(choice_button("../res/image/背包选项.png", (536,283+y*40),font3, itemlevel[y] +"物品剩余数量"+str(self.itemnum[1][y])))
                for y in range(0,4):
                    self.item[2].append (choice_button("../res/image/背包选项.png", (536,515+y*40),font3, itemlevel[y] +"物品剩余数量"+str(self.itemnum[2][y])))
                for y in range(0,4):
                    self.item[3].append(choice_button("../res/image/背包选项.png", (973,515+y*40),font3, itemlevel[y] +"物品剩余数量"+str(self.itemnum[3][y])))
                self.fish = []
                self.fish.append(choice_button("../res/image/背包选项.png", (536, 727), font3, "喂猫：物品剩余"+str(self.itemnum[4])))
                self.fish.append(choice_button("../res/image/背包选项.png", (536, 767), font3, "食用：物品剩余"+str(self.itemnum[4])))
                self.apple = choice_button("../res/image/背包选项.png", (973, 747), font3, "吃水果：物品剩余"+str(self.itemnum[5]))
            def update(self,pressed):
                for x in range(0,4):
                    for y in range(0,4):
                        if self.item[x][y].update(pressed) == 1:
                            return x , y
                if self.fish[0].update(pressed) == 1:
                    return 4, 5
                if self.fish[1].update(pressed) == 1:
                    return 4, 6
                if self.apple.update(pressed) == 1:
                    return 5, 5
                if self.close.update(pressed) == 1:
                    return 4 , 4
                return -2 , -2
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.close.print(self.screen)
                self.fish[0].print(self.screen)
                self.fish[1].print(self.screen)
                self.apple.print(self.screen)
                for x in range(0,4):
                    for y in range(0,4):
                        self.item[x][y].print(self.screen)

                
        #test        
        #testbutton = button("../res/image/退出游戏0.png","../res/image/退出游戏1.png",(640,585), "../res/sound/button.mp3", "../res/sound/press.wav")
        
        
        #开始
        cat_run = 0 #判断猫猫是否出动
        rolltimes = 0
        hvrolled = 0
        student = stu(10,10,10,2,10,32,3.0)
        te , now_event_id= spawn_event(student.state)
        now_event_solved = 0
        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
        day = 1
        cat_xinguan = 0
        can_go = 0
        resteve = 0            
        eveshown = 0
        bagshown = 0
        now_item = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0,0]
        now_bag = bag(self, now_item)
        

        if start_item[0] == -1:
            #继续游戏
            save1 = save.split()
            student = stu(int(save1[0]),int(save1[1]),int(save1[2]),int(save1[3]),int(save1[4]),int(save1[5]),float(save1[6]))
            student.too_low = [int(save1[7]),int(save1[8]),int(save1[9]),int(save1[10]),int(save1[11])]
            student.without_fruit = int(save1[12])
            now_item = [[int(save1[13]),int(save1[14]),int(save1[15]),int(save1[16])],
                        [int(save1[17]),int(save1[18]),int(save1[19]),int(save1[20])],
                        [int(save1[21]),int(save1[22]),int(save1[23]),int(save1[24])],
                        [int(save1[25]),int(save1[26]),int(save1[27]),int(save1[28])],
                        int(save1[29]),int(save1[30])]
            day = int(save1[31])
            cat_run = int(save1[32])
            rolltimes = int(save1[33])
            student.wangwang = [int(save1[34]),int(save1[35]),int(save1[36]),int(save1[37]),int(save1[38]),int(save1[39])]
            student.exam = int(save1[40])
            student.go_out = int(save1[41])

            te , now_event_id= spawn_event(student.state)
            now_event_solved = 0
            now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
        else:
            now_item = Randdraw.getdraw(start_item)
            student.exam = random.randint(5,10)
            with open('save1.txt', 'w') as f:
                save = ""
                for i in range(0,6):
                    save = save + str(student.state[i])+" "
                save = save + str(student.gpa)+" "
                for i in range(0,5):
                    save = save + str(student.too_low[i])+" "
                save = save + str(student.without_fruit)+" "
                for i in range(0,4):
                    for j in range(0,4):
                        save = save + str(now_item[i][j])+" "
                save = save + str(now_item[4])+" "
                save = save + str(now_item[5])+" "
                save = save + str(day)+" "
                save = save + str(cat_run)+" "
                save = save + str(rolltimes)+" "
                for i in range(0,6):
                    save = save + str(student.wangwang[i])+" "
                save = save + str(student.exam)+" "
                save = save + str(student.go_out)+" "
                f.write(save)

        #画面组件
        nextmove = choice_button("../res/image/选项.png", (850, 800), font1 , "确认" )
        nextday = choice_button("../res/image/选项.png", (630, 880), font1 , "上床睡觉！" )
        openevent = choice_button1("../res/image/事件余.png" , (900 , 800) , eventpFont , "事件余"+str(resteve))
        refreshevent = choice_button1("../res/image/事件余.png" , (370 , 800) , eventpFont , "刷新事件")
        marketroll = choice_button1("../res/image/超市摇号.png" , (880 , 72) , eventpFont , "摇号")
        examclock = choice_button2("../res/image/考试.png" , (880 , 216) , eventpFont3 , "还有"+str(student.exam)+"天考试")
        openbag = choice_button1("../res/image/背包.png" , (1100 , 800) , eventpFont , "背包")
        state_bar = []
        state_bar.append(state("饥饿值",(10 , 10000 , 200 , 10000) , (205,104,57)))
        state_bar.append(state("口渴值",(10 , 10000 , 300 , 10000) , (99,184,255)))
        state_bar.append(state("san值",(10 , 10000 , 400 , 10000) , (191,62,255)))
        state_bar.append(state("智商",(10 , 10000 , 500 , 10000) , (0,250,154)))
        state_bar.append(state("清洁值",(10 , 10000 , 600 , 10000) , (255,240,245)))
        day_queue = []
        time_queue = []
        message_queue = []
        timeword_min = ["00","15","30","45"]
        timeword_hour = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]


        #！！有特别效果的事件 连续事件返回0 否则返回1
        def specialeffect(eventid , chosen):
            
            if eventid == 5 and chosen == 1:
                student.hesuan += 1
                
            if eventid == 11 and chosen == 0 :
                student.wangwang[0] = 1
            if eventid == 11 and chosen == 1 :
                student.wangwang[1] = 1  
            if eventid == 11 and chosen == 2 :
                student.wangwang[4] = 1 
            if eventid == 12 and chosen == 0 :
                student.wangwang[3] = 1  
            if eventid == 12 and chosen == 1 :
                student.wangwang[5] = 1
                
            if eventid == 10 and chosen == 0 :
                student.wangwang[2] = 1

            if eventid == 16 and chosen == 0:
                student.ET = 1

            #连续事件
            if eventid == 17 and chosen == 0:#跳转至18
                te = EventList.evelist[18]
                now_event_id = 18
                tnow_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                return tnow_event , now_event_id , 0

            if eventid == 17 and chosen == 1:#跳转至19
                te = EventList.evelist[19]
                now_event_id = 19
                tnow_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                return tnow_event , now_event_id , 0

            if eventid == 22 and chosen == 0:
                student.go_out += 1

            if eventid == 24 and chosen == 0 or eventid == 34 and chosen == 0 :
                student.quality[0] += 1
            
            if eventid == 31 and chosen == 0 :
                student.quality[1] += 1

            if eventid == 29 and chosen == 0 :
                student.quality[2] += 1
            
            if eventid == 33 and chosen == 0 :
                student.quality[3] += 1
             
            if eventid == 23 and chosen == 0 :
                student.quality[4] += 1

            if evnetid == 35 and chosen == 0 :   #背包物品增加
                now_item[0][1] += 2
                now_item[1][1] += 2
            
            if evnetid == 35 and chosen == 1 :
                now_item[0][1] += 1
                now_item[1][1] += 1
            
            return now_event , eventid , 1
            
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
                    if GamePause.pause(self,2) == 1:
                        return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if GamePause.pause(self,2) == 1:
                            return -1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = [1]

        #结局检测
            if student.too_low[0] >= 5:
                return 0
            if student.too_low[1] >= 5:
                return 1
            if student.hesuan >= 3:
                return 2
            if cat_xinguan == 1:
                return 3
            if student.wangwang[2] == 1:
                return 4
            if student.ET == 1:
                return 5
            if student.go_out == 2:
                return 6
            if student.quality[0] >= 1 and student.quality[1] >= 1 and student.quality[2] >= 1 and student.quality[3] >= 1 and student.quality[4] >= 1 : 
                return 7
        #更新图像

            #更换寝室背景：
            if cat_run == 0:
                bg = pygame.image.load("../res/image/寝室.png").convert()
            else:
                bg = pygame.image.load("../res/image/寝室1.png").convert()
                
            now_bag = bag(self, now_item)
            #consume_result x , y
            if bagshown == 1:
                crx , cry = now_bag.update(pressed)
                if crx >= 0 and cry >= 0:
                    if crx == 4 and cry == 4:
                        bagshown = 0
                    elif cry >= 5 and now_item[crx] == 0:
                        now_event.tipstime = 30
                        now_event.tipstr = "物品不足！"
                    elif cry < 5 and now_item[crx][cry] == 0:
                        now_event.tipstime = 30
                        now_event.tipstr = "物品不足！"
                    else:
                        #这里写物品效果
                        if crx == 0:
                            if student.state[1] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "喝不下啦！"
                            else:
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("喝了一瓶饮料，口渴值+"+str(4-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                cons = [0,4-cry,0,0,0,0]
                                if student.state[1] <= 3:
                                    cons[5] = 2
                                elif student.state[1] >= 8:
                                    cons[5] = 4
                                else:
                                    cons[5] = 3
                                student.updatestate(cons)

                        if crx == 1:
                            if student.state[0] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "吃不下啦！"
                            else:
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("吃了一餐，饥饿值+"+str(4-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                cons = [4-cry,0,0,0,0,0]
                                if student.state[0] <= 3:
                                    cons[5] = 2
                                elif student.state[0] >= 8:
                                    cons[5] = 4
                                else:
                                    cons[5] = 3
                                student.updatestate(cons)
                                

                        if crx == 2:
                            if len(message_queue) == 6:
                                del message_queue[0]
                                del day_queue[0]
                                del time_queue[0]
                            time_queue.append(student.state[5])
                            day_queue.append(day)
                            message_queue.append("认真学习，智商+"+str(6-cry)+",饥饿值-2，口渴值-2，清洁值-2")
                            now_item[crx][cry] -= 1
                            bagshown = 0
                            cons = [-2,-2,0,6-cry,-2,0]
                            if student.state[3] <= 4:
                                cons[5] = 12
                            elif student.state[3] >= 7:
                                cons[5] = 8
                            else:
                                cons[5] = 10                           
                            student.updatestate(cons)
                                
                        if crx == 3:
                            if student.state[4] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "很干净啦！"
                            else:
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("洗了个澡，清洁值+"+str(6-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                cons = [0,0,0,0,6-cry,0]
                                if student.state[4] <= 2:
                                    cons[5] = 6
                                elif student.state[4] >= 6:
                                    cons[5] = 2
                                else:
                                    cons[5] = 4
                                student.updatestate(cons)

                        if crx == 4:
                            if cry == 5:#喂猫 
                                if cat_run != 0:
                                    now_event.tipstime = 30
                                    now_event.tipstr = "猫猫队已经出动辣！"
                                else:
                                    if len(message_queue) == 6:
                                        del message_queue[0]
                                        del day_queue[0]
                                        del time_queue[0]
                                    time_queue.append(student.state[5])
                                    day_queue.append(day)
                                    cat_run = 1
                                    cat_day = random.randint(3,6)
                                    message_queue.append("给猫猫喂鱼了，猫猫队出动,猫猫预计会在"+str(cat_day - 1)+"后归来")
                                    now_item[4] -= 1
                                    bagshown = 0
                                    cons = [0,0,0,0,0,2]
                                    student.updatestate(cons)
                            if cry == 6: #吃鱼
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("生吃了个鱼，饥饿值+2，口渴值 + 2，清洁值 -1")
                                now_item[4] -= 1
                                bagshown = 0
                                cons = [2,2,0,0,-1,2]
                                student.updatestate(cons)

                        if crx == 5:
                            if len(message_queue) == 6:
                                del message_queue[0]
                                del day_queue[0]
                                del time_queue[0]
                            time_queue.append(student.state[5])
                            day_queue.append(day)
                            message_queue.append("吃了些水果，新鲜维他命！感到状态好极了，饥饿值+2，口渴值+2")
                            now_item[crx] -= 1
                            bagshown = 0
                            cons = [2,2,0,0,0,2]
                            student.updatestate(cons)
                            student.without_fruit = 0
                            
            if eveshown == 1:
                if now_event.chosen != -1:
                        
                    if now_event_solved == 0:
                        if len(message_queue) == 6:
                            del message_queue[0]
                            del day_queue[0]
                            del time_queue[0]
                        time_queue.append(student.state[5])
                        day_queue.append(day)
                        message_queue.append(EventList.message[now_event_id][now_event.chosen])
                        student.updatestate(EventList.effect[now_event_id][now_event.chosen])
                        now_event , now_event_id , now_event_solved = specialeffect(now_event_id , now_event.chosen)
                        
                    if now_event_solved == 1:
                        if now_event.update(student , now_event_id, pressed) == 1 or nextmove.update(pressed) == 1:
                            eveshown = 0
                            resteve -= 1
                            te, now_event_id =spawn_event(student.state)
                            now_event_solved = 0
                            now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                    
                if now_event.update(student , now_event_id, pressed) == 1:
                    eveshown = 0
                    
            if eveshown == 0 and bagshown == 0:
                if openevent.update(pressed) == 1:
                    eveshown = 1
                    if resteve == 0:
                        eveshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "当前没有事件哦"
                    if student.state[5] >= 88 or student.state[5] < 32:
                        eveshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                    if student.exam == 0:
                        eveshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去考试啦！！！"
                    
                if openbag.update(pressed) == 1:
                    bagshown = 1
                    if student.state[5] >= 88 or student.state[5] < 32:
                        bagshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                    if student.exam == 0:
                        bagshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去考试啦！！！"
                        
                if refreshevent.update(pressed) == 1:
                    if student.state[5] >= 88 or student.state[5] < 32:
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                    elif resteve == 3:
                        now_event.tipstime = 30
                        now_event.tipstr = "事件太多啦！！！"
                    elif student.exam == 0:
                        now_event.tipstime = 30
                        now_event.tipstr = "该去考试啦！！！"
                    else:
                        resteve += 1
                        if len(message_queue) == 6:
                            del message_queue[0]
                            del day_queue[0]
                            del time_queue[0]
                        time_queue.append(student.state[5])
                        day_queue.append(day)
                        message_queue.append("摸了半小时鱼，又有新事件要处理了")
                        cons = [0,0,0,0,0,2]
                        student.updatestate(cons)
                #事件超时
                if resteve > 0:
                    if EventList.refreshneed[now_event_id][5] != 10000 and EventList.refreshneed[now_event_id][6] != 10000:
                        if EventList.refreshneed[now_event_id][5] != 0 or EventList.refreshneed[now_event_id][6] != 0:
                            if EventList.refreshneed[now_event_id][5] > student.state[5] or student.state[5] > EventList.refreshneed[now_event_id][6]:
                                resteve -= 1
                                te, now_event_id =spawn_event(student.state)
                                now_event_solved = 0
                                now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("呀好像忘了啥，事件超时已消失")
                
                if marketroll.update(pressed) == 1:
                    if student.state[5] >= 88 or student.state[5] < 32:
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                    elif student.exam == 0:
                        now_event.tipstime = 30
                        now_event.tipstr = "该去考试啦！！！"
                    else:
                        if hvrolled == 1:
                            now_event.tipstime = 30
                            now_event.tipstr = "今天摇过号了呢"
                        else:   
                            hvrolled = 1
                            rollnum = random.randint(0,99)
                            rolltimes += 1
                            if rollnum > 95 or rolltimes >= 10:
                                can_go = 1
                                rolltimes = 0
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("中了！明天8点起床就可以去超市了！")
                            else:
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("没中，可惜")
                            cons = [0,0,0,0,0,2]
                            student.updatestate(cons)
                        
                if examclock.update(pressed) == 1:
                    if student.exam == 0:
                        if len(message_queue) == 6:
                            del message_queue[0]
                            del day_queue[0]
                            del time_queue[0]
                        time_queue.append(student.state[5])
                        day_queue.append(day)
                        examscore = random.randint(0,100) + 2*student.state[2]
                        if examscore >= 70:
                            student.gpa += 0.3
                            message_queue.append("考试真简单，我还想多考点，GPA+0.3")
                        elif examscore <= 20:
                            student.gpa -= 1
                            message_queue.append("糟了考砸了，GPA-1.0")
                        else:
                            message_queue.append("考的一般般，还好勉强及格了")
                        cons = [0,0,0,0,0,10]
                        student.updatestate(cons)
                        student.exam = random.randint(5,10)
                    else:
                        now_event.tipstime = 30
                        now_event.tipstr = "还没到考试时间"
                    
            if student.state[5] >= 88 or student.state[5] < 32:
                if nextday.update(pressed) == 1:
                    resteve = 0
                    day += 1
                    hvrolled = 0
                    student.exam -= 1
                    #睡觉动画maybe
                    tmpstate = []
                    for i in range(0,5):
                        tmpstate.append(student.state[i])
                    student.updatestate([-2,-2,0,0,-2,0])
                    student.state[5] = 32
                    student.without_fruit += 1
                    if len(message_queue) == 6:
                        del message_queue[0]
                        del day_queue[0]
                        del time_queue[0]
                    time_queue.append(student.state[5])
                    day_queue.append(day)
                    tmpmessage = "一觉醒来，"
                    tmpmessage = tmpmessage + "饥饿值-" + str(tmpstate[0]-student.state[0]) + "，"
                    tmpmessage = tmpmessage + "口渴值-" + str(tmpstate[1]-student.state[1]) + "，"
                    tmpmessage = tmpmessage + "清洁值-" +str(tmpstate[4]-student.state[4]) + "，"
                    tmpmessage = tmpmessage + "未处理的事件已清空"
                    message_queue.append(tmpmessage)
                    if cat_run != 0:
                        cat_run += 1
                        if cat_run == cat_day:#猫猫归来
                            cat_run = 0
                            cat_level = random.randint(0,99)
                            if cat_level < 97: #猫猫带回来物资
                                cat_item = [random.randint(1,3),random.randint(1,3),random.randint(0,2),random.randint(0,2),random.randint(0,1),random.randint(0,1)]
                                cat_item1 = Randdraw.getdraw(cat_item)
                                for x in range(0,4):
                                    for y in range(0,4):
                                        now_item[x][y] += cat_item1[x][y]
                                now_item[4] += cat_item1[4]
                                now_item[5] += cat_item1[5]
                                if len(message_queue) == 6:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("猫猫带回来了不少物资，快去背包看看吧！")
                            else:
                                cat_xinguan = 1
                    if can_go == 1:
                        can_go = 0
                        self.fill((0,0,0))
                        result = Supermarket.Game1(self)
                        earned_item = Randdraw.getdraw(result)
                        for i in range(0,4):
                            for j in range(0,4):
                                now_item[i][j] += earned_item[i][j]
                        now_item[4] += earned_item[4]
                        now_item[5] += earned_item[5]
                        if len(message_queue) == 6:
                            del message_queue[0]
                            del day_queue[0]
                            del time_queue[0]
                        time_queue.append(student.state[5])
                        day_queue.append(day)
                        message_queue.append("出发去采购！")
                        cons = [0,0,0,0,0,12]
                        student.updatestate(cons)
                        if len(message_queue) == 6:
                            del message_queue[0]
                            del day_queue[0]
                            del time_queue[0]
                        time_queue.append(student.state[5])
                        day_queue.append(day)
                        message_queue.append("采购结束，快去背包看看吧！")
                    te, now_event_id =spawn_event(student.state)
                    now_event_solved = 0
                    now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)

                    #存档
                    with open('save1.txt', 'w') as f:
                        save = ""
                        for i in range(0,6):
                            save = save + str(student.state[i])+" "
                        save = save + str(student.gpa)+" "
                        for i in range(0,5):
                            save = save + str(student.too_low[i])+" "
                        save = save + str(student.without_fruit)+" "
                        for i in range(0,4):
                            for j in range(0,4):
                                save = save + str(now_item[i][j])+" "
                        save = save + str(now_item[4])+" "
                        save = save + str(now_item[5])+" "
                        save = save + str(day)+" "
                        save = save + str(cat_run)+" "
                        save = save + str(rolltimes)+" "
                        for i in range(0,6):
                            save = save + str(student.wangwang[i])+" "
                        save = save + str(student.exam)+" "
                        save = save + str(student.go_out)+" "
                        f.write(save)
                    
            openevent.text = "事件余"+str(resteve)
            examclock.text = "还有"+str(student.exam)+"天考试"
            if student.exam == 0:
                examclock.text = "出发去考试"
            pressed[0] = 0
            
        #打印图像
            self.blit(bg , (0,0))
            self.blit(message_bg , (950,0))
            
            message_cnt = 0
            for message in message_queue:
                word_print((1000 , 1200 , 40+message_cnt*100 , 70+message_cnt*100), "[Day"+str(day_queue[message_cnt])+"  "+str(timeword_hour[time_queue[message_cnt]//4])+":"+str(timeword_min[time_queue[message_cnt] % 4]+"]") , timefont2 , (0,255,255))
                word_print((1000 , 1200 , 65+message_cnt*100 , 170+message_cnt*100), message , messagefont , (255 ,255 ,255))
                message_cnt += 1
                
            for i in range(0,5):
                state_bar[i].print(self,student.state[i])
            word_print((10 , 10000 , 100 , 10000), "Time  "+str(timeword_hour[student.state[5]//4])+":"+str(timeword_min[student.state[5] % 4]) , timefont , (0,255,0))
            word_print((10 , 10000 , 700 , 10000), "GPA  "+str(round(student.gpa,1)) , gpafont , (255,0,0))
            word_print((10 , 10000 , 10 , 10000), "第  "+str(day)+"  天" , gpafont , (255,255,0))
            if student.without_fruit >= 10:
                word_print((10 , 280 , 800 , 10000), "缺乏维生素，口腔溃疡了，每次吃东西的时候都会疼得不能思考QAQ" , font2 , (100,100,255))
            openevent.print(self)
            openbag.print(self)
            refreshevent.print(self)
            marketroll.print(self)
            examclock.print(self)
            
            if student.state[5] >= 88 or student.state[5] < 32:
                nextday.print(self)
            if bagshown == 1:
                now_bag.print_event()
            if eveshown == 1:
                now_event.print_event()
                if now_event.chosen != -1:
                    nextmove.print(self)
            if now_event.tipstime > 0:
                word_print((400,10000,20,10000) , now_event.tipstr, tipsfont, (255,255,255))
                now_event.tipstime -= 2

            
            # #testpart
            # buttons = pygame.mouse.get_pressed()
            # pos = pygame.mouse.get_pos()            
            # text0 = "mouse position: " + str(pos)
            # text0_surface = testfont.render(text0, True, (255, 0, 0))
            # self.blit(text0_surface, (10, 50))
            
        #刷新屏幕
            pygame.display.flip()
