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
    #属性顺序 饥饿值 口渴值 san值 智商 清洁值 时间（以小时为单位，影响每日事件进度）
    #0
    evelist.append(eve("../res/image/test事件.png","今天又9:40起床了，要不要choco捏",2 ,["cho!","不cho!"] , ["好cho!(智商降低)","冲去上课，满身是汗(清洁值降低)"]))
    effect.append([[0,0,0,-1,0, 4],[0,0,0,0,-1, 4]])
    #1
    evelist.append(eve("../res/image/test事件.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生!(饥饿缓解，清洁降低)","..."]))
    effect.append([[+1,0,0,0,-1, 2],[0,0,0,0,0, 2]])
    #2

    #...
