import sys
import pygame

class EventList:
    class eve:
        def __init__(self , image , text , choice_num , choice_text , resulttext):
            self.image = image
            self.text = text
            self.choice_num = choice_num
            self.choice_text = choice_text
            self.resulttext = resulttext
    evelist = []
    effect = []
    
    #0
    evelist.append(eve("../res/image/test事件.png","今天又9:40起床了，要不要choco捏",2 ,["cho!","不cho!"] , ["好cho!(智商降低)","冲去上课，满身是汗(清洁值降低)"]))
    effect.append([[0,0,0,-1,0],[0,0,0,0,-1]])
    #1
    #2
    #...
