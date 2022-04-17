import sys
import pygame

class Ending:
                
    def print(self , ending_num):
        
        #设置背景

        ending_image = pygame.image.load("../res/image/ending"+str(ending_num)+".png").convert()
        
        #设置音效
        pygame.mixer.init()
        #记得改！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        pygame.mixer.music.load("../res/sound/宿舍BGM.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        #文本打印函数
        font = pygame.freetype.Font("../res/font/Pixel.ttf",35)
        font.antialiased = False
        
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

        #设置按钮
        
        conti = choice_button("../res/image/选项.png", (400, 800), font , "返回主菜单" )
        exi = choice_button("../res/image/选项.png", (800, 800), font , "退出游戏" )

        #创建时钟对象（控制游戏的FPS）
        clock = pygame.time.Clock()
        
        #结局部分主循环
                
        while True:

        #锁60帧
            clock.tick(60)
        #处理事件
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = [1]

                
        #更新图像
            if conti.update(pressed) == 1:
                return -1
            if exi.update(pressed) == 1:
                return 0
                   
            pressed[0] = 0
            
        #打印图像
            self.blit(ending_image , (0,0))
            conti.print(self)
            exi.print(self)
            
            
        #刷新屏幕
            pygame.display.flip()

        return -1
        #返回是否回主菜单
