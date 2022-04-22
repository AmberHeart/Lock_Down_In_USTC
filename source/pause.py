import sys
import pygame
import pygame.freetype
from tips import Tips

class GamePause:

    def pause(self, stage):

        #设置字体
        font1 = pygame.freetype.Font("../res/font/Pixel.ttf",100)
        font1.antialiased = False
        font1.origin = True

        font2 = pygame.freetype.Font("../res/font/Pixel.ttf",30)
        font2.antialiased = False

        #设置音乐
        pygame.mixer.init()
        pause_sound = pygame.mixer.Sound("../res/sound/pause.wav")
        pause_sound.set_volume(0.4)
        pause_sound.play()
        
        #设置暂停界面背景
        bg_image = pygame.image.load("../res/image/暂停背景.png").convert()
        bg_x = 240
        bg_y = 100

        #文本打印函数
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


        continuebutton = button("../res/image/选项.png" , (640 , 420) , font2 , "继续游戏" )
        mainbutton = button("../res/image/选项.png" , (640 , 570) , font2 , "返回主菜单" )
        exitbutton = button("../res/image/选项.png" , (640 , 720) , font2 , "退出游戏" )
        
        #创建时钟对象（控制游戏的FPS）
        clock = pygame.time.Clock()
        
        #暂停部分主循环
                
        while True:

        #锁60帧
            clock.tick(60)
        #处理事件
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return 0
        #更新按钮
            if continuebutton.update() == 1:
                return 0
            if mainbutton.update() == 1:
                if Tips.Show(self,stage) == 1:
                    return 1
            if exitbutton.update() == 1:
                if Tips.Show(self,stage) == 1:
                    pygame.quit()
                    sys.exit()
        #打印图像
            self.blit(bg_image , (bg_x, bg_y))
            continuebutton.print(self)
            mainbutton.print(self)
            exitbutton.print(self)
        #打印文本
            font1.get_rect("暂 停 中")
            font1.render_to(self, (440,300),None, (255,255,255))
        #刷新屏幕
            pygame.display.flip()
