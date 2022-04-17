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
        eventfont = pygame.freetype.Font("../res/font/Pixel.ttf",40)
        eventfont.antialiased = False
        statefont = pygame.freetype.Font("../res/font/Pixel.ttf",15)
        statefont.antialiased = False
        gpafont = pygame.freetype.Font("../res/font/Pixel.ttf",40)
        gpafont.antialiased = False
        tipsfont = pygame.freetype.Font("../res/font/Pixel.ttf",30)
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

        #提示持续时间
        
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
                    
                
        #玩家类
        
        class stu:
            #饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) GPA
            def __init__(self, hungry, thirsty, san, iq, clean , day_time , gpa):
                self.state = [hungry,thirsty,san,iq,clean,day_time]
                #GPA
                self.gpa = gpa
                #buff or debuff
                self.buff = []

            def updatestate(self):

                dailyconsume = [-2,-2,0,0,-2]
                for i in range(0,5):
                    self.state[i] += dailyconsume[i]
                    if self.state[i] < 0:
                        student.state[i] = 0
                    if self.state[i] > 10:
                        student.state[i] = 10
                self.state[5] = 32

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
        
        def spawn_event():
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
        class bag: #!先用上事件的贴图了
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
            def update(self,pressed):
                for x in range(0,4):
                    for y in range(0,4):
                        if self.item[x][y].update(pressed) == 1:
                            return x , y
                if self.close.update(pressed) == 1:
                    return 4 , 4
                return -2 , -2
            def print_event(self):
                self.screen.blit(self.bg_image, self.bg_image_topleft)
                self.close.print(self.screen)
                for x in range(0,4):
                    for y in range(0,4):
                        self.item[x][y].print(self.screen)
                
        #test        
        #testbutton = button("../res/image/退出游戏0.png","../res/image/退出游戏1.png",(640,585), "../res/sound/button.mp3", "../res/sound/press.wav")
        
        
        #开始
        te , now_event_id= spawn_event()
        now_event_solved = 0
        now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
        student = stu(10,10,10,2,10,32,3.0)
        day = 1

        resteve = 1            
        eveshown = 0
        bagshown = 0
        now_item = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0],[0]]
        now_bag = bag(self, now_item)
        
        if start_item[0] == -1:
            #继续游戏
            continu = 1
        else:
            now_item = Randdraw.getdraw(start_item)

        #画面组件
        nextmove = choice_button("../res/image/选项.png", (850, 800), font1 , "确认" )
        nextday = choice_button("../res/image/选项.png", (630, 880), font1 , "上床睡觉！" )
        openevent = choice_button("../res/image/事件余.png" , (900 , 800) , font1 , "事件余"+str(resteve))
        openbag = choice_button("../res/image/背包.png" , (1100 , 800) , font1 , "背包")
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

                
        #更新图像

            now_bag = bag(self, now_item)
            #consume_result x , y
            if bagshown == 1:
                crx , cry = now_bag.update(pressed)
                if crx >= 0 and cry >= 0:
                    if crx == 4 and cry == 4:
                        bagshown = 0
                    elif now_item[crx][cry] == 0:
                        now_event.tipstime = 30
                        now_event.tipstr = "物品不足！"
                    else:
                        #这里写物品效果
                        if crx == 0:
                            if student.state[1] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "喝不下啦！"
                            else:
                                if len(message_queue) == 7:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("喝了一瓶饮料，口渴值+"+str(4-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                if student.state[1] <= 3:
                                    student.state[5] += 2
                                elif student.state[1] >= 8:
                                    student.state[5] += 4
                                else:
                                    student.state[5] += 3
                                student.state[1] += 4-cry
                                if student.state[1] > 10:
                                    student.state[1] = 10

                        if crx == 1:
                            if student.state[0] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "吃不下啦！"
                            else:
                                if len(message_queue) == 7:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("吃了一餐，饥饿值+"+str(4-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                if student.state[0] <= 3:
                                    student.state[5] += 2
                                elif student.state[0] >= 8:
                                    student.state[5] += 4
                                else:
                                    student.state[5] += 3
                                student.state[0] += 4-cry
                                if student.state[0] > 10:
                                    student.state[0] = 10
                                

                        if crx == 2:
                            if len(message_queue) == 7:
                                del message_queue[0]
                                del day_queue[0]
                                del time_queue[0]
                            time_queue.append(student.state[5])
                            day_queue.append(day)
                            message_queue.append("认真学习，智商+"+str(6-cry)+",饥饿值-2，口渴值-2，清洁值-2")
                            now_item[crx][cry] -= 1
                            bagshown = 0
                            if student.state[3] <= 4:
                                student.state[5] += 12
                            elif student.state[3] >= 7:
                                student.state[5] += 8
                            else:
                                student.state[5] += 10
                            student.state[0] -= 2
                            student.state[1] -= 2
                            student.state[4] -= 2
                            student.state[3] += 6-cry
                            if student.state[0] < 0:
                                student.state[0] = 0
                            if student.state[1] < 0:
                                student.state[1] = 0
                            if student.state[4] < 0:
                                student.state[4] = 0
                            if student.state[3] > 10:
                                student.state[3] = 10
                                
                        if crx == 3:
                            if student.state[4] == 10:
                                now_event.tipstime = 30
                                now_event.tipstr = "很干净啦！"
                            else:
                                if len(message_queue) == 7:
                                    del message_queue[0]
                                    del day_queue[0]
                                    del time_queue[0]
                                time_queue.append(student.state[5])
                                day_queue.append(day)
                                message_queue.append("洗了个澡，清洁值+"+str(6-cry))
                                now_item[crx][cry] -= 1
                                bagshown = 0
                                if student.state[4] <= 2:
                                    student.state[5] += 6
                                elif student.state[4] >= 6:
                                    student.state[5] += 2
                                else:
                                    student.state[5] += 4
                                student.state[4] += 6-cry
                                if student.state[4] > 10:
                                    student.state[4] = 10
                                
            if eveshown == 1:
                if now_event.update(student , now_event_id, pressed) == 1:
                    eveshown = 0
                    
            if eveshown == 0 and bagshown == 0:
                if openevent.update(pressed) == 1:
                    eveshown = 1
                    if resteve == 0:
                        eveshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                if openbag.update(pressed) == 1:
                    bagshown = 1
                    if resteve == 0:
                        bagshown = 0
                        now_event.tipstime = 30
                        now_event.tipstr = "该去睡觉啦！！！"
                        
            if now_event.chosen != -1:

                if now_event_solved == 0:
                    if len(message_queue) == 7:
                        del message_queue[0]
                        del day_queue[0]
                        del time_queue[0]
                    time_queue.append(student.state[5])
                    day_queue.append(day)
                    message_queue.append(EventList.message[now_event_id][now_event.chosen])
                    for i in range(0,5):
                        student.state[i] += EventList.effect[now_event_id][now_event.chosen][i]
                        if student.state[i] < 0:
                            student.state[i] = 0
                        if student.state[i] > 10:
                            student.state[i] = 10
                    student.state[5] += EventList.effect[now_event_id][now_event.chosen][5]
                    if student.state[5] >= 96:
                        student.state[5] -= 96
                now_event_solved = 1
                
                if nextmove.update(pressed) == 1:
                    #生成新事件
                    eveshown = 0
                    te, now_event_id =spawn_event()
                    now_event_solved = 0
                    now_event = choose_event(self , te.image , font1 , te.text , te.choice_num , te.choice_text, te.resulttext)
                    
            if student.state[5] >= 88 or student.state[5] < 32:
                if nextday.update(pressed) == 1:
                    day += 1
                    resteve = 1
                    #睡觉动画maybe
                    tmpstate = []
                    for i in range(0,5):
                        tmpstate.append(student.state[i])
                    student.updatestate()
                    if len(message_queue) == 7:
                        del message_queue[0]
                        del day_queue[0]
                        del time_queue[0]
                    time_queue.append(student.state[5])
                    day_queue.append(day)
                    tmpmessage = "一觉醒来，"
                    tmpmessage = tmpmessage + "饥饿值-" + str(tmpstate[0]-student.state[0]) + "，"
                    tmpmessage = tmpmessage + "口渴值-" + str(tmpstate[1]-student.state[1]) + "，"
                    tmpmessage = tmpmessage + "清洁值-" +str(tmpstate[4]-student.state[4])
                    message_queue.append(tmpmessage)
                    
            openevent.text = "事件余"+str(resteve)
            pressed[0] = 0
            
        #打印图像
            self.blit(bg , (0,0))

            message_cnt = 0
            for message in message_queue:
                word_print((1000 , 1200 , message_cnt*100 , 30+message_cnt*100), "[Day"+str(day_queue[message_cnt])+"  "+str(timeword_hour[time_queue[message_cnt]//4])+":"+str(timeword_min[time_queue[message_cnt] % 4]+"]") , timefont2 , (0,255,255))
                word_print((1000 , 1200 , 25+message_cnt*100 , 130+message_cnt*100), message , messagefont , (255 ,255 ,255))
                message_cnt += 1
                
            for i in range(0,5):
                state_bar[i].print(self,student.state[i])
            word_print((10 , 10000 , 100 , 10000), "Time  "+str(timeword_hour[student.state[5]//4])+":"+str(timeword_min[student.state[5] % 4]) , timefont , (0,255,0))
            word_print((10 , 10000 , 700 , 10000), "GPA  "+str(student.gpa) , gpafont , (255,0,0))
            word_print((10 , 10000 , 10 , 10000), "第  "+str(day)+"  天" , gpafont , (255,255,0))
            openevent.print(self)
            openbag.print(self)

            if student.state[5] >= 88 or student.state[5] < 32:
                nextday.print(self)
                resteve = 0
            if bagshown == 1:
                now_bag.print_event()
            if eveshown == 1:
                now_event.print_event()
                if now_event.chosen != -1:
                    nextmove.print(self)
            if now_event.tipstime > 0:
                word_print((500,10000,20,10000) , now_event.tipstr, tipsfont, (255,0,0))
                now_event.tipstime -= 1
            
            #testpart
            buttons = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()            
            text0 = "mouse position: " + str(pos)
            text0_surface = testfont.render(text0, True, (255, 0, 0))
            self.blit(text0_surface, (10, 50))
            
        #刷新屏幕
            pygame.display.flip()
