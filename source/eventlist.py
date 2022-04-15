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
            
    #事件总数，每次加事件的时候记得改
    event_num = 3
    
    evelist = []
    #属性增减 饥饿值 口渴值 san值 智商 清洁值 时间(单位15min)
    effect = []
    #无要求就是-1 时间要求不计在此处
    limit = []
    

    #0
    evelist.append(eve("../res/image/test事件.png","今天又9:40起床了，要不要choco捏",2 ,["cho!","不cho!"] , ["好cho!(智商降低)","冲去上课，满身是汗(清洁值降低)"]))
    effect.append([[0,0,0,-1,0,4],[0,0,0,0,-1,4]])
    limit.append([[-1,-1,-1,1,-1],[-1,-1,-1,-1,-1]])
    #1
    evelist.append(eve("../res/image/test事件.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生!(饥饿缓解，清洁降低)","..."]))
    effect.append([[+1,0,0,0,-1, 1],[0,0,0,0,0, 1]])
    limit.append([[-1,-1,-1,-1,1],[-1,-1,-1,-1,-1]])
    #2
    evelist.append(eve("../res/image/test事件.png","小咪亿下",1 ,["睡！"] , ["zzZZZZZZZZ..."]))
    effect.append([[0,0,0,0,0,48]])
    limit.append([[-1,-1,-1,-1,-1]])
    #3
    #...
