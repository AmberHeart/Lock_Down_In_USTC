#导入模块
import sys
import pygame
import random

class Dormitory:
    
    def Game2(self,start_item):
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
        #创建时钟对象（控制游戏的FPS）

        clock = pygame.time.Clock()

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
            
        class stu:
            #饥饿值
            hungry = 100
            #口渴值
            thirsty = 100
            #san值
            san = 100
            #清洁值
            clean = 100
            #GPA
            gpa = 3.0

        def spawn_event():
            judge_num = random.randint()
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

        testbutton = button("../res/image/退出游戏0.png","../res/image/退出游戏1.png",(640,585),"../res/sound/button.mp3","../res/sound/press.wav")
        
        #宿舍部分主循环
                
        while True:

        #锁60帧
            clock.tick(60)
        #处理事件
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        #更新图像
            if testbutton.update() == 1:
                pygame.quit()
                sys.exit()
                return -1
            
        #打印图像
            self.blit(testbutton.image,testbutton.rect)
            pygame.display.flip()
