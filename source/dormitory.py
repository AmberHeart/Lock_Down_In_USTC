#导入模块
import sys
import pygame
import random
import pygame.freetype

class Dormitory:
    
    def Game2(self,start_item):
        #设置音效
        pygame.mixer.init()
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        #文本打印函数
        font1 = pygame.freetype.Font("../res/font/Pixel.ttf",45)
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

        #玩家类
        
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

        #随机事件
        
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

        #计数器
        day = 0
        
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
        #更新图像
            if testbutton.update() == 1:
                pygame.quit()
                sys.exit()
                return -1

        #打印文本
            word_print((200,400,200,400),"00000000000000000000000000xxxxxxxxx00000000000",font1)
            
        #打印图像
            self.blit(testbutton.image,testbutton.rect)
            pygame.display.flip()
