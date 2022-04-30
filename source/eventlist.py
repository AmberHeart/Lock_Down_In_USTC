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

    #事件总数，每次加事件的时候记得改。
    event_num = 13
    
    evelist = []
    #属性增减 饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) (单个事件的时间不要超过37)
    effect = []
    #选选项的需求 最小值）无要求就是0 时间要求不计在此处
    limit = []
    #做出选择后在状态栏出现的信息
    message = []
    #刷出该事件的需求，无要求为0 最后两项为时间下限和上限 范围在32~88之间 无要求则同时为0
    refreshneed = []

    #! 有特殊影响的事件在dormitory中的specialeffect处添加！！！
    
    #时间对照: ( 8:00 -> 32 ) ( 22:00 -> 88 )
        
    #0
    evelist.append(eve("../res/image/要迟到了.png","早上睡迟了，要不要翘课呢",2 ,["翘！","不翘！"] , ["翘的好！","冲去上课，满身是汗"]))
    effect.append([[0,0,0,-1,0,4],[0,0,0,0,-1,4]])
    limit.append([[0,0,0,1,0],[0,0,0,0,0]])
    message.append(["翘课睡觉咯，智商-1","冲去上课，满身是汗，清洁值-1"])
    refreshneed.append([0,0,0,0,0,32,40])
    #1
    evelist.append(eve("../res/image/老坛酸菜.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生！","..."]))
    effect.append([[+1,0,0,0,-1, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,1],[0,0,0,0,0]])
    message.append(["吃了老坛酸菜牛肉面，饥饿值+1，清洁值-1","谢绝了隔壁老铁的老坛酸菜牛肉面"])
    refreshneed.append([0,0,0,0,0,0,0])
    #2
    evelist.append(eve("../res/image/睡觉.png","小咪亿下",1 ,["睡！"] , ["zzZZZZZZZZ..."]))
    effect.append([[0,0,0,0,0,36]])
    limit.append([[0,0,0,0,0]])
    message.append(["小睡了9个小时"])
    refreshneed.append([0,0,0,0,0,0,0])
    #3
    evelist.append(eve("../res/image/夜间读书.png","要熄灯了，要不要偷偷读书呢",2 ,["偷偷读","直接睡觉了"] , ["拿着手电筒在被窝里读书，可惜效率不高","zzZZZZZZ"]))
    effect.append([[0,0,-2,1,0,8],[0,0,0,0,1,4]])
    limit.append([[0,0,2,0,0],[0,0,0,0,0]])
    message.append(["秉灯夜读，san值-2，智商+1","刷牙洗脸睡咯，清洁值+1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #4
    evelist.append(eve("../res/image/自习室.png","好朋友邀你去自习室卷卷",2 ,["出发！","不去，在床上摆烂了"] , ["自习了好久，感觉学会了不少东西呢","摸鱼摸的好爽"]))
    effect.append([[0,0,0,2,0,12],[0,0,2,-2,0,4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["自习了3个小时，智商+2","摸鱼摸了1个小时，非常快乐，san值+2，智商-2"])
    refreshneed.append([0,0,0,0,0,32,88])
    #5 周常核酸检测
    evelist.append(eve("../res/image/核酸检测.png","核酸检测",2 ,["马上去做","叛逆！不去！"] , ["排了一条从图书馆到操场超长大队，终于做了核酸，嗓子好痛","在宿舍里边吃零食边卷卷，舒服了"]))
    effect.append([[0,0,0,0,0,24],[0,0,0,2,0,12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["排了一条从图书馆到操场超长大队，终于做了核酸","在宿舍舒适地卷卷，智商+2"])
    refreshneed.append([0,0,0,0,0,56,88])
    #6 敲门 查卫生
    evelist.append(eve("../res/image/哐哐哐敲门.png","叮叮当,有人敲门", 2 ,["开门","一定有鬼,不开"] , ["宿管查卫生,寄！","..."]))
    effect.append([[0,0,-1,0,+1, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["┭┮﹏┭┮ 被迫整理 san值-1 清洁值+1","不开门好像不太好"])
    refreshneed.append([0,0,0,0,0,48,60])
    #7敲门 送六个核桃
    evelist.append(eve("../res/image/咚咚咚敲门.png","咚咚咚,有人敲门", 2 ,["开门","一定有鬼,不开"] , ["隔壁朋友送来六个核桃,提神醒脑","..."]))
    effect.append([[0,0,0,+1,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["喝了六个核桃 智商+1","不开门好像不太好"])
    refreshneed.append([0,0,0,0,0,48,88])
    #8砸门 恶作剧
    evelist.append(eve("../res/image/砸门.png","哐哐哐,有人砸门", 2 ,["战战兢兢开门","这回真滴一定有鬼,坚决不开"] , ["门口空无一人","..."]))
    effect.append([[0,0,-5,0,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["没人。。。 san值-5","不应该开门"])
    refreshneed.append([0,0,0,0,0,48,88])
    #9二课读书 崩了
    evelist.append(eve("../res/image/二课.png","室友拉你去参加悦读二课", 2 ,["好耶","算了，万一二课又崩了"] , ["好书啊好书，不过二课果然崩了","还好没去，二课崩了"]))
    effect.append([[0,0,-1,+1,0, 8],[0,0,0,+1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["读书收获 智商+1 签到失败 san值-1","暗自庆幸 san值+1"])
    refreshneed.append([0,0,0,0,0,48,88])
    #10旺旺（隐藏，特定条件触发，伪装成砸门）
    evelist.append(eve("../res/image/砸门.png","哐哐哐,有人砸门", 2 ,["战战兢兢开门","这回真滴一定有鬼,坚决不开"] , ["有人送来旺仔牛奶糖！","..."]))
    effect.append([[1,0,10,0,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["吃掉旺仔牛奶糖，美滋滋，san回满","不应该开门"])
    refreshneed.append([0,0,0,0,0,32,88])
    #11旺旺1
    evelist.append(eve("../res/image/旺旺大礼包.jpg","好兄弟买了旺旺大礼包", 3 ,["好耶，来个雪饼","好耶，来个仙贝","好耶，来个挑豆"] , ["不错，还顶饱","不错，顶饱","不错，但是好像更饿了"]))
    effect.append([[1,0,0,+1,0, 1],[1,0,0,0,0, 1], [-1,0,0,0,0,1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["吃了个旺旺雪饼，饥饿值+1","吃了个旺旺仙贝，饥饿值+1","吃了挑豆，饥饿值-1"])
    refreshneed.append([0,0,0,0,0,48,88])
    #12旺旺2
    evelist.append(eve("../res/image/旺旺大礼包.jpg","好兄弟买了旺旺大礼包", 2 ,["好耶，来罐旺仔牛奶","好耶，来包粟米条"] , ["不错，好喝","味不错，就是太甜"]))
    effect.append([[0,1,0,0,0, 1],[0,-1,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["喝了旺仔牛奶，口渴值+1","吃了旺旺粟米条，不管饱，口渴值-1"])
    refreshneed.append([0,0,0,0,0,48,88])
