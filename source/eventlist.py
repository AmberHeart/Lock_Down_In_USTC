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
    event_num = 94
    
    evelist = []
    #属性增减 饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) (单个事件的时间不要超过37)
    effect = []
    #选选项的需求 最小值）无要求就是0 时间要求不计在此处
    limit = []
    #做出选择后在状态栏出现的信息
    message = []
    #刷出该事件的需求，无要求为0 最后两项为时间下限和上限 范围在32~88（即8~22点）之间 无要求则同时为0
    refreshneed = []

    #! 有特殊影响的事件在dormitory中的specialeffect处添加！！！
    
    #时间对照: ( 8:00 -> 32 ) ( 22:00 -> 88 )
        
    #0 翘课事件
    evelist.append(eve("../res/image/要迟到了.png","早上睡迟了，要不要翘课呢",2 ,["翘！","不翘！"] , ["翘的好！","冲去上课，满身是汗"]))
    effect.append([[0,0,0,-1,0,4],[0,0,0,0,-1,4]])
    limit.append([[0,0,0,1,0],[0,0,0,0,0]])
    message.append(["翘课睡觉咯，智商-1","冲去上课，满身是汗，清洁值-1"])
    refreshneed.append([0,0,0,0,0,32,40])
    #1 老坛酸菜  
    evelist.append(eve("../res/image/老坛酸菜.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生！","..."]))
    effect.append([[+1,0,0,0,-1, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,1],[0,0,0,0,0]])
    message.append(["吃了老坛酸菜牛肉面，饥饿值+1，清洁值-1","谢绝了隔壁老铁的老坛酸菜牛肉面"])
    refreshneed.append([0,0,0,0,0,50,80])  #小改了一下时间，老坛频率太高有点掉SAN
    #2 零星小睡
    evelist.append(eve("../res/image/睡觉.png","小咪亿下",1 ,["睡！"] , ["zzZZZZZZZZ..."]))
    effect.append([[0,0,0,0,0,12]])
    limit.append([[0,0,0,0,0]])
    message.append(["小睡了3个小时"])
    refreshneed.append([0,0,0,0,0,48,56])
    #3 夜间读书
    evelist.append(eve("../res/image/夜间读书.png","要熄灯了，要不要偷偷读书呢",2 ,["偷偷读","直接睡觉了"] , ["拿着手电筒在被窝里读书，可惜效率不高","zzZZZZZZ"]))
    effect.append([[0,0,-2,1,0,8],[0,0,0,0,1,4]])
    limit.append([[0,0,2,0,0],[0,0,0,0,0]])
    message.append(["秉灯夜读，san值-2，智商+1","刷牙洗脸睡咯，清洁值+1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #4 自习室事件
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
    refreshneed.append([0,0,0,0,0,48,72])
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
    effect.append([[0,0,-3,0,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["没人。。。 san值-3","不应该开门"])
    refreshneed.append([0,0,0,0,0,48,88])
    #9二课读书 崩了
    evelist.append(eve("../res/image/二课.png","室友拉你去参加悦读二课", 2 ,["好耶","算了，万一二课又崩了"] , ["好书啊好书，不过二课果然崩了","还好没去，二课崩了"]))
    effect.append([[0,0,-1,+1,0, 8],[0,0,1,0,0, 8]])
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
    effect.append([[1,0,0,0,0, 1],[1,0,0,0,0, 1], [-1,0,0,0,0,1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["吃了个旺旺雪饼，饥饿值+1","吃了个旺旺仙贝，饥饿值+1","吃了挑豆，饥饿值-1"])
    refreshneed.append([0,0,0,0,0,48,88])
    #12旺旺2
    evelist.append(eve("../res/image/旺旺大礼包.jpg","好兄弟买了旺旺大礼包", 2 ,["好耶，来罐旺仔牛奶","好耶，来包粟米条"] , ["不错，好喝","味不错，就是太甜"]))
    effect.append([[0,1,0,0,0, 1],[0,-1,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["喝了旺仔牛奶，口渴值+1","吃了旺旺粟米条，不管饱，口渴值-1"])
    refreshneed.append([0,0,0,0,0,48,88])
    #13 小霸王游戏机
    evelist.append(eve("../res/image/小霸王.png","朋友发来一个链接打开后发现是小霸王", 2 ,["开玩！","算了，还是学习吧"] , ["对大学生来说刚刚好！","学习使我快乐捏~"]))
    effect.append([[0,0,+1,-1,0, 8],[0,0,-1,+1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["玩了两小时 智商-1  san值+1","学了两小时 san值-1 智商+1"])
    refreshneed.append([0,0,0,0,0,0,0])
    #14 夜聊事件
    evelist.append(eve("../res/image/夜聊.png","晚上收到了消息", 2 ,["发生甚么事了","假装没看到睡大觉"] , ["聊了很晚，困死了","睡完大觉感到愧疚"]))
    effect.append([[0,0,0,-1,0, 12],[0,0,-1,0,0, 12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["好困啊 智商-1","有点愧疚 san值-1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #15 额外食品供应事件
    evelist.append(eve("../res/image/额外食品.png","今天有额外食物供应，你的到了", 2 ,["立刻去取","这题还没做完，等会再去吧"] , ["饱餐一顿","被人拿走了QAQ"]))
    effect.append([[+1,+1,+1,0,0, 2],[0,0,-1,-1,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["饥饿值+1 口渴值+1 san值+1","过于气愤 智商-1 san值-1"])
    refreshneed.append([0,0,0,0,0,44,56])
    #16 静谧的夜1（带一个魔幻结局）
    evelist.append(eve("../res/image/诡异的光.jpg","阳台有一束诡异的光", 2 ,["去看看吧","管他呢睡大觉"] , ["外星人来咯","无事发生..."]))
    effect.append([[0,0,0,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,7,7,0],[0,0,0,0,0]])  #san和智商均大于7才能触发该结局
    message.append(["已经结束咧","无事发生"])
    refreshneed.append([0,0,0,0,0,84,88])
    #17 （板子用）  连续事件开头   好友申请
    evelist.append(eve("../res/image/好友申请.jpg","收到一条好友申请", 2 ,["有什么事吗？同意","这谁啊？拒绝"] , ["同意","拒绝"]))
    effect.append([[0,0,0,0,0, 2],[0,0,0,0,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["同意","拒绝"])
    refreshneed.append([0,0,0,0,0,80,88])
    #18 （板子用 记得替换） 卖茶事件
    evelist.append(eve("../res/image/卖茶.jpg","交流了一会儿...", 2 ,["没什么吧","速删了"] , ["没删","删除"]))
    effect.append([[0,0,-1,-1,0, 2],[0,0,-1,-1,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["被诈骗 智商-1 san值-1","删后遭到持续申请很烦 san值-1 智商-1"])
    refreshneed.append([0,0,0,0,0,10000,10000])#标记为无法自然刷出 作为事件17的子事件1
    #19 （板子用 记得替换） 警察来咯
    evelist.append(eve("../res/image/警察.jpg","不久后一个电话自称警察...", 2 ,["积极反映了事件","普通配合就好"] , ["过于积极遭怀疑","接受反诈教育"]))
    effect.append([[0,0,0,-1,0, 2],[0,0,0,+1,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["过于积极遭遇怀疑 智商-1","接受了反诈教育 智商+1"])
    refreshneed.append([0,0,0,0,0,10000,10000])#标记为无法自然刷出 作为事件17的子事件2
    #20 沉迷学习
    evelist.append(eve("../res/image/沉迷学习.jpg","早早起来精神抖擞可以去图书馆大卷一天",2 ,["出发！","不去，在床上摆烂了"] , ["卷了一天，忘了吃饭","摸鱼摸的好爽"]))
    effect.append([[-3,0,-3,5,0,32],[0,0,+2,-2,0,4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["废寝忘食连续了8个小时，饥饿-3，san值-3，智商+5","摸鱼摸了1个小时，非常快乐，san值+2，智商-2"])
    refreshneed.append([0,0,0,0,0,32,36])
    #21 疲惫学习
    evelist.append(eve("../res/image/沉迷学习.jpg","早早被室友闹钟叫醒，好困，要不要去图书馆",2 ,["出发！","不去，还没睡醒"] , ["好困，早知道不出来了","好睡！"]))
    effect.append([[0,0,-3,1,0,8],[0,0,+2,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["很困的学习，效率很低，san值-3，智商+1","又睡了2个小时，感觉好多了，san值+2"])
    refreshneed.append([0,0,0,0,0,32,36])
    #22 出去玩
    evelist.append(eve("../res/image/出去玩.jpg","最近心情很不好（真滴么。。），偷偷出去嗨一下吧",2 ,["出发！","算了算了，防疫要紧"] , ["玩爽了","无事发生"]))
    effect.append([[0,0,3,-5,0,28],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["玩嗨了，san值+3，智商-5","无事发生"])
    refreshneed.append([0,0,0,0,0,40,48])
    #23 志愿者
    evelist.append(eve("../res/image/志愿者.png","芳草社招防疫志愿者咯",2 ,["马上参加","算了算了，还是在寝室睡大觉"] , ["为同学们服务，感觉真好","..."]))
    effect.append([[0,0,3,0,0,20],[0,0,0,0,0,8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["参加志愿服务，san值+3","无事发生"])
    refreshneed.append([0,0,0,0,0,32,60])
    #24 讲座
    evelist.append(eve("../res/image/讲座.png","老一辈科学家来讲座咯",2 ,["马上参加","算了算了，还是在寝室睡大觉"] , ["学习了老一辈科学家精神","..."]))
    effect.append([[0,0,0,0,0,20],[0,0,0,0,0,8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["参加老科学家讲座，提升道德素质","无事发生"])
    refreshneed.append([0,0,0,0,0,32,60])
    #25 讲座忘记出校报备
    evelist.append(eve("../res/image/讲座.png","老一辈科学家来讲座咯",2 ,["马上参加","算了算了，还是在寝室睡大觉"] , ["糟了，忘报备了，寄！","..."]))
    effect.append([[0,0,-1,0,0,12],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["忘记报备被卡门外，san值-1","无事发生"])
    refreshneed.append([0,0,0,0,0,32,60])
    #26 习题课
    evelist.append(eve("../res/image/习题课.jpg","晚上有习题课",2 ,["去上课","不去了，估计没什么人去吧"] , ["有所收获","有点后悔，会不会错过重要内容。"]))
    effect.append([[0,0,+2,0,0,8],[0,0,-1,0,0,8]])
    limit.append([[0,0,5,5,0],[0,0,0,0,0]])
    message.append(["习题课有所收获，智商+2","后悔ing，san值-1"])
    refreshneed.append([0,0,0,0,0,72,76])
    #27 习题课，但没听懂
    evelist.append(eve("../res/image/习题课.jpg","晚上有习题课",2 ,["去上课","不去了，估计没什么人去吧"] , ["有所收获，但好多没听懂","估计去了也听不懂"]))
    effect.append([[0,0,+1,-2,0,8],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["习题课有所收获，但心情低落，智商+1，san值-2","无事发生"])
    refreshneed.append([0,0,0,0,0,72,76])
    #28 去健身
    evelist.append(eve("../res/image/健身.png","好久没活动身体，去健身吧",2 ,["走起","不去了，累= ="] , ["浑身是汗，爽了","窝里蹲"]))
    effect.append([[-1,-1,0,+1,-1,8],[0,0,0,0,0,8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["运动带来好心情，不过出了好多汗，饥饿-1，口渴-1，san值+1，清洁值-1","无事发生"])
    refreshneed.append([0,0,0,0,0,50,80])
    #29 线上运动会
    evelist.append(eve("../res/image/线上运动会.png","疫情期间开展线上运动会小活动",2 ,["有点意思，参加一下","看看热闹算了"] , ["取得了好成绩！","体育活动与我无缘"]))
    effect.append([[-1,-1,0,+2,-1,20],[0,0,0,0,0,8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["成绩不错美滋滋，不过出了好多汗，饥饿-1，口渴-1，san值+2，清洁值-1","emm，下次参加吧"])
    refreshneed.append([0,0,0,0,0,50,80])
    #30 线上运动会，未取得成绩
    evelist.append(eve("../res/image/线上运动会.png","疫情期间开展线上运动会小活动",2 ,["有点意思，参加一下","看看热闹算了"] , ["成绩一般，不过重在参与","体育活动与我无缘"]))
    effect.append([[0,0,0,+1,-1,20],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["重在参与，不过出了好多汗，san值+1，清洁值-1","emm，下次参加吧"])
    refreshneed.append([0,0,0,0,0,50,80])
    #31 竞赛（赢）
    evelist.append(eve("../res/image/竞赛.png","学院举办XX竞赛咯",2 ,["火速报名","不去了，估计没什么人去吧"] , ["成绩不错哟","竞赛不是我能伸的上手的"]))
    effect.append([[0,0,+2,0,0,16],[0,0,0,0,0,8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["参加竞赛学会了新知识，智商+2","摆就完了"])
    refreshneed.append([0,0,0,0,0,32,48])
    #32 竞赛（输）
    evelist.append(eve("../res/image/竞赛.png","学院举办XX竞赛咯",2 ,["火速报名","不去了，估计没什么人去吧"] , ["参加后才发现自己这么菜","竞赛不是我能伸的上手的"]))
    effect.append([[0,0,0,-2,0,16],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["我好弱，好难过，san值-2","摆就完了"])
    refreshneed.append([0,0,0,0,0,32,48])
    #33 诗歌鉴赏
    evelist.append(eve("../res/image/诗歌鉴赏.png","星云诗社开展诗歌鉴赏活动",2 ,["火速报名","没文化鉴赏不得，还是学数理"] , ["能探风雅无穷意，始是乾坤绝妙词","我莫得文化"]))
    effect.append([[0,0,0,0,0,16],[0,0,+2,0,0,16]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["陶冶了情操","还是打好数理基础，智商+2"])
    refreshneed.append([0,0,0,0,0,32,72])
    #34 学习党史
    evelist.append(eve("../res/image/学党史.png","不忘初心，学习党史",2 ,["积极参加，继承先辈意志","还是学数理"] , ["提升道德素质，心怀国之大者","你说的不算，学党史！"]))
    effect.append([[0,0,0,0,0,16],[0,0,0,0,0,16]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["学党史","学党史"])
    refreshneed.append([0,0,0,0,0,32,72])
    #35 静谧的夜2
    evelist.append(eve("../res/image/诡异的光.jpg","阳台有一束诡异的光", 2 ,["去看看吧","管他呢睡大觉"] , ["原来是只猫...","有什么带来了食物..."]))
    effect.append([[0,0,+1,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,5,5,0],[0,0,0,0,0]])  #该情况触发条件比1宽松，算是给玩家的线索
    message.append(["原来是只猫 san值+1 食物+2 饮品+2","食物+1 饮品+1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #36 静谧的夜3
    evelist.append(eve("../res/image/诡异的光.jpg","阳台有一束诡异的光", 2 ,["去看看吧","管他呢睡大觉"] , ["隔壁寝室的兄弟居然来偷吃","阳台上的食物离奇减少"]))
    effect.append([[-1,0,0,0,-1, 8],[-2,-1,0,0,0, 8]])
    limit.append([[0,0,5,5,0],[0,0,0,0,0]])  #该情况触发条件比1宽松，算是给玩家的线索
    message.append(["正义阻止偷吃 清洁值-1 饥饿值-1","饥饿值-2 口渴值-1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #37 连续事件开头  理发事件（第三个选项没有分支）
    evelist.append(eve("../res/image/理发.png","要不要去理发呢", 3 ,["偷偷去校外理发","校内解决吧","不响理辣"] , ["去校外","在校内","不响理辣"]))
    effect.append([[0,0,0,0,0, 2],[0,0,0,0,0, 2],[0,0,0,0,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["校外理发","校内理发","不响理辣"])
    refreshneed.append([0,0,0,0,0,60,68])
    #38 校外理发
    evelist.append(eve("../res/image/校外理发.jpg","有很多店呢", 2 ,["去更华丽的那家","去朴素的那家吧"] , ["被骗办卡","普通地理了发"]))
    effect.append([[0,0,0,-1,+1, 8],[0,0,0,-1,+1, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["被骗办卡 智商-2 清洁+1","简单地理发但被发现出校 智商-1 清洁+1"])
    refreshneed.append([0,0,0,0,0,10000,10000])#标记为无法自然刷出 作为事件37的子事件1
    #39 校内理发
    evelist.append(eve("../res/image/校内理发.jpg","可是校内的毁发中心...", 2 ,["去学校理发店","自己动手！"] , ["新发型但是头发有点少","成功坑到了自己"]))
    effect.append([[0,0,-1,0,+1, 4],[0,0,0,-1,0, 6]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["一言难尽的发型 san值-1 清洁+1","没事自己乱来啥 智商-1"])
    refreshneed.append([0,0,0,0,0,10000,10000])#标记为无法自然刷出 作为事件38的子事件2
    #40 数分习题事件
    evelist.append(eve("../res/image/数分习题.jpg","这是一道数分习题", 2 ,["答案4PI","答案是2PI"] , ["回答正确","回答错误"]))
    effect.append([[0,0,0,+1,0, 4],[0,0,0,-2,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["恭喜答对 智商+1","答错了很可惜 智商-2"])
    refreshneed.append([0,0,0,0,0,48,80])
    #41 ddl过多造成抑郁
    evelist.append(eve("../res/image/补作业.jpg","盘点最近积攒的作业", 2 ,["狂补！","先休息一下吧"] , ["终于完成了","早晚还是要写的"]))
    effect.append([[0,0,0,-2,0, 8],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["写了好久，好累...","慢慢做吧，细水长流"])
    refreshneed.append([0,0,0,0,0,48,80])
    #42 ddl前置 数学
    evelist.append(eve("../res/image/数学.png","数学作业太多了", 2 ,["写作业！","摆！"] , ["终于完成了","舒服了"]))
    effect.append([[0,0,0,0,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,8,0],[0,0,0,0,0]])  
    message.append(["完成了数学作业","没完成数学作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #43 ddl前置 物理
    evelist.append(eve("../res/image/物理.jpg","物理作业好难", 2 ,["写作业！","摆！"] , ["终于完成了","舒服了"]))
    effect.append([[0,0,0,0,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,6,0],[0,0,0,0,0]])  
    message.append(["完成了物理作业","没完成物理作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #44 ddl前置 英语
    evelist.append(eve("../res/image/英语.jpg","英语作业好麻烦", 2 ,["写作业！","摆！"] , ["终于完成了","舒服了"]))
    effect.append([[0,0,0,0,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,5,0],[0,0,0,0,0]])  
    message.append(["完成了英语作业","没完成英语作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #45 本草纲目
    evelist.append(eve("../res/image/本草纲目.jpg","刘畊宏邀请你一起健身", 2 ,["健身","开躺！"] , ["很累但是很快乐","想躺就躺"]))
    effect.append([[0,0,+1,0,-1, 8],[0,0,0,-2,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["一言难尽的发型 san值+1 清洁-1","没事自己乱来啥 智商-2"])
    refreshneed.append([0,0,0,0,0,48,80])
    #46 大物实验
    evelist.append(eve("../res/image/大物实验.jpg","大物实验将进行实验报告评讲", 2 ,["去听听吧","开躺！"] , ["听了但没完全听","想躺就躺"]))
    effect.append([[0,0,0,+1,0, 8],[0,0,0,-2,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["没完全懂但有所收获 智商+1","好躺！ 智商-2"])
    refreshneed.append([0,0,0,0,0,72,80])
    #47 发呆
    evelist.append(eve("../res/image/发呆.jpg","突然好想发呆捏", 2 ,["发呆...","不发，开卷！"] , ["满足了捏","完全没用"]))
    effect.append([[0,0,+1,0,0, 8],[0,0,0,-1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["发呆两小时 san值+1","卷了，但是没卷 智商-1"])
    refreshneed.append([0,0,0,0,0,48,72])
    #48 青年大学习（夹带私货）
    evelist.append(eve("../res/image/青年大学习.jpg","新一期的青年大学习来咯", 2 ,["学学我的","好麻烦，不学了"] , ["学的好","快点去学"]))
    effect.append([[0,0,0,+1,0, 8],[0,0,0,-2,0, 8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["学的好 智商+1","快点去学 智商-2"])
    refreshneed.append([0,0,0,0,0,52,60])
    #49 MBTI测试事件
    evelist.append(eve("../res/image/MBTI.jpg","有人推荐你做MBTI测试", 2 ,["测一下试试","不测了"] , ["自己找一个测吧ヽ(*´з｀*)ﾉ","无事发生"]))
    effect.append([[0,0,0,0,0, 4],[0,0,0,0,0, 2]])
    limit.append([[0,0,8,0,0],[0,0,0,0,0]])
    message.append(["自己找一个测吧ヽ(*´з｀*)ﾉ","无事发生"])
    refreshneed.append([0,0,0,0,0,56,68])
    #50 大物实验预习测
    evelist.append(eve("../res/image/大物实验.jpg","大物实验要来了，先做一下预习测？", 2 ,["开做","过会在做"] , ["完成了预习测","坏了，本来想过会做结果忘了"]))
    effect.append([[0,0,0,0,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["预习测完成","忘做预习测血亏，san值-2"])
    refreshneed.append([0,0,0,5,0,50,76])
    #51 大物实验出门测
    evelist.append(eve("../res/image/大物实验.jpg","大物实验做完了，赶快做一下出门测？", 2 ,["开做","过会在做"] , ["完成了出门测","坏了，本来想过会做结果忘了"]))
    effect.append([[0,0,0,0,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["出门测完成","忘做出门测血亏，san值-2"])
    refreshneed.append([0,0,0,5,0,76,88])
    #52 研讨课
    evelist.append(eve("../res/image/研讨课.jpg","组长又来催研讨课进度了", 2 ,["开做","我摆"] , ["众人拾柴火焰高","摸鱼爽，一直模一直爽"]))
    effect.append([[0,0,+1,+1,0, 8],[0,0,+1,0,0, 8]])
    limit.append([[0,0,5,0,0],[0,0,0,0,0]])
    message.append(["在研讨课中成长，协作中感受个人价值 智商+1 san值+1","摸鱼真舒服 san值+1"])
    refreshneed.append([0,0,0,0,0,32,84])
    #53 研讨课（摸鱼被逮）
    evelist.append(eve("../res/image/研讨课.jpg","组长又来催研讨课进度了", 2 ,["开做","我摆"] , ["众人拾柴火焰高","坏，摸鱼被组长发现"]))
    effect.append([[0,0,+1,+1,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["在研讨课中成长，协作中感受个人价值 智商+1 san值+1","摸鱼被逮了 san值-2"])
    refreshneed.append([0,0,0,0,0,32,84])
    #54 给学校建议
    evelist.append(eve("../res/image/提建议.jpg","有机会给学校提建议了", 3 ,["大物实验有点多，可否减少","量子物理有点难，可否改为选修","没什么可提捏"] , ["已经减少过了","这是我们的特色","确实"]))
    effect.append([[0,0,0,0,0, 8],[0,0,0,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["原来已经减少过了..QAQ","只好学了QAQ","emm"])
    refreshneed.append([0,0,0,0,0,32,50])
    #55 上课（网课？）
    evelist.append(eve("../res/image/网课.jpg","该上课啦，但是懒得动", 2 ,["去上课吧","寝室看bb平台算了"] , ["挣扎爬到教学楼","寝室上课舒服"]))
    effect.append([[0,0,0,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["上课是个体力活","寝室上课舒服捏"])
    refreshneed.append([0,0,0,0,0,32,80])
    #56 上课被点名
    evelist.append(eve("../res/image/网课.jpg","该上课啦，但是懒得动", 2 ,["去上课吧","寝室看bb平台算了"] , ["点名了，还好去了","坏了，点名了，成翘课人了"]))
    effect.append([[0,0,0,0,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["上课是个体力活","被点名点中 san值-2"])
    refreshneed.append([0,0,0,0,0,32,80])
    #57 心情不好听音乐
    evelist.append(eve("../res/image/听音乐.jpg","有些emo，听听音乐吧", 2 ,["听点轻音乐","听听高燃神曲"] , ["有点忧伤..","燃起来了！！！"]))
    effect.append([[0,0,-1,0,0, 8],[0,0,1,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["音乐让人忧伤 san值-1","音乐让失意者振奋 san值+1"])
    refreshneed.append([0,0,0,0,0,32,80])
    #58 心情好听音乐
    evelist.append(eve("../res/image/听音乐2.jpg","有点无聊，听听音乐吧", 2 ,["听点轻音乐","听听高燃神曲"] , ["心如止水","燃起来了！！！"]))
    effect.append([[0,0,1,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["音乐让人清醒 san值+1","音乐让人振奋"])
    refreshneed.append([0,0,0,0,0,32,80])
    #59 大雾实验报告
    evelist.append(eve("../res/image/大雾实验.jpg","做完大物实验了，去写实验报告吧", 2 ,["写","还是写"] , ["写..写完了","写..完了"]))
    effect.append([[0,0,0,0,0, 12],[0,0,0,0,0, 12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["累！","累！"])
    refreshneed.append([0,0,0,0,0,32,60])
    #60 Ta邀请约会
    evelist.append(eve("../res/image/情侣.jpg","Ta约你出去", 2 ,["好耶！","不去，专注学业"] , ["开心","智者不如爱河.."]))
    effect.append([[0,0,1,0,0, 12],[0,0,0,0,0, 12]])
    limit.append([[0,0,0,0,8],[0,0,0,0,0]])
    message.append(["和Ta出去玩 san值+1","学习，不过不知为什么今天效率好低"])
    refreshneed.append([0,0,0,0,0,32,60])
    #61 Ta邀请去学习
    evelist.append(eve("../res/image/情侣学习.jpg","Ta约你去学习", 2 ,["好耶！","不去，还是自己学习"] , ["开心","寡王直通硕博.."]))
    effect.append([[0,0,1,0,0, 12],[0,0,-1,1,0, 12]])
    limit.append([[0,0,0,0,8],[0,0,0,0,0]])
    message.append(["和Ta去学习，开心，但是心里都是Ta，学不进去 san值+1","学习，但是好失落，san值-1，智商+1"])
    refreshneed.append([0,0,0,0,0,32,72])
    #62 Ta邀请去学习2
    evelist.append(eve("../res/image/情侣学习.jpg","Ta约你去学习", 2 ,["好耶！","不去，还是自己学习"] , ["开心，学习变得快乐","智者不如爱河.."]))
    effect.append([[0,0,1,1,0, 12],[0,0,-1,1,0, 12]])
    limit.append([[0,0,0,0,8],[0,0,0,0,0]])
    message.append(["和Ta去学习，开心，学习效率倍增 san值+1 智商+1","学习，但是好失落，san值-1，智商+1"])
    refreshneed.append([0,0,0,0,0,32,72])
    #63 Ta邀请打游戏
    evelist.append(eve("../res/image/情侣玩游戏.jpg","Ta约你打游戏", 2 ,["好耶！","不去，专注学业"] , ["被Ta吐槽打得菜TAT","我选择学习"]))
    effect.append([[0,0,-1,0,0, 8],[0,0,0,1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["和Ta玩崩了.. san值-1","下次找我学习 智商+1"])
    refreshneed.append([0,0,0,0,0,32,60])
    #64 Ta邀请打游戏2
    evelist.append(eve("../res/image/情侣玩游戏.jpg","Ta约你打游戏", 2 ,["好耶！","不去，自己打"] , ["直接带飞(*^▽^*)","孤独上分"]))
    effect.append([[0,0,+1,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,7,0],[0,0,0,0,0]])
    message.append(["打的不错，san值+1","无聊上（掉）分ing"])
    refreshneed.append([0,0,0,0,0,32,60])
    #65 大学生创业
    evelist.append(eve("../res/image/大学生创业.jpg","学长传授创业知识", 2 ,["去了解","好像和现在的我无关"] , ["收获很大","前途茫茫"]))
    effect.append([[0,0,0,0,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["早晚会走出校门，应该提前准备","早晚会走出校门，应该提前准备"])
    refreshneed.append([0,0,0,0,0,32,72])
    #66 大物实验预习测(负效果)
    evelist.append(eve("../res/image/大物实验.jpg","大物实验要来了，先做一下预习测？", 2 ,["开做","过会在做"] , ["完成了预习测","坏了，本来想过会做结果忘了"]))
    effect.append([[0,0,-1,0,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["预习测完成，但是错了一堆，san值-1","忘做预习测血亏，san值-2"])
    refreshneed.append([0,0,0,0,0,50,76])
    #67 大物实验出门测（负效果）
    evelist.append(eve("../res/image/大物实验.jpg","大物实验做完了，赶快做一下出门测？", 2 ,["开做","过会在做"] , ["完成了出门测","坏了，本来想过会做结果忘了"]))
    effect.append([[0,0,-1,0,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["出门测完成，但是错了一堆，san值-1","忘做出门测血亏，san值-2"])
    refreshneed.append([0,0,0,0,0,76,88])
    #68 研讨课（负效果）
    evelist.append(eve("../res/image/研讨课.jpg","组长又来催研讨课进度了", 2 ,["开做","我摆"] , ["太难了","坏，摸鱼被组长发现"]))
    effect.append([[0,0,-2,-1,0, 8],[0,0,-2,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["完全没头绪 智商-2 san值-1","摸鱼被逮了 san值-2"])
    refreshneed.append([0,0,0,0,0,32,84])
    #69 发呆（负效果）
    evelist.append(eve("../res/image/发呆.jpg","突然好想发呆捏", 2 ,["发呆...","不发，开卷！"] , ["做有意义的事情不好吗","完全没用"]))
    effect.append([[0,0,-2,0,0, 8],[0,0,0,-1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["发呆两小时，痛恨自己浪费时间 san值-2","卷了，但是没卷 智商-1"])
    refreshneed.append([0,0,0,0,0,48,72])
    #70 ddl前置 英语（负效果）
    evelist.append(eve("../res/image/英语.jpg","英语作业好麻烦", 2 ,["写作业！","摆！"] , ["单词认识我，我不认识它","舒服了"]))
    effect.append([[0,0,-1,0,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["我咋啥也看不懂？san值-1","没完成英语作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #71 ddl前置 数学（负效果）
    evelist.append(eve("../res/image/数学.png","数学作业太多了", 2 ,["写作业！","摆！"] , ["这啥证明题？？这也要证？这也能证？","舒服了"]))
    effect.append([[0,0,-1,-1,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["受到数学作业摧残 san值-1 智商-1","没完成数学作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #72 ddl前置 物理（负效果）
    evelist.append(eve("../res/image/物理.jpg","物理作业好难", 2 ,["写作业！","摆！"] , ["这公式好像都用不到题里","舒服了"]))
    effect.append([[0,0,-1,-1,0, 4],[0,0,+1,0,0, 4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["受到物理作业摧残 san值-1 智商-1","没完成物理作业"])
    refreshneed.append([0,0,0,0,0,48,80])
    #73 MBTI测试事件（负效果）
    evelist.append(eve("../res/image/MBTI.jpg","有人推荐你做MBTI测试", 2 ,["测一下试试","不测了"] , ["自己找一个测吧ヽ(*´з｀*)ﾉ","无事发生"]))
    effect.append([[0,0,-3,0,0, 4],[0,0,0,0,0, 2]])
    limit.append([[0,0,8,0,0],[0,0,0,0,0]])
    message.append(["发现自己疑似抑郁，很难受 san值-3","无事发生"])
    refreshneed.append([0,0,0,0,0,56,68])
    #74 周常核酸检测（负效果）
    evelist.append(eve("../res/image/核酸检测.png","核酸检测",2 ,["马上去做","叛逆！不去！"] , ["发现今天没有核酸检测","在宿舍里边吃零食边卷卷，但是还是担心出问题"]))
    effect.append([[0,0,-2,0,0,24],[0,0,-2,1,0,12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["白去了 san值-2","在宿舍卷卷却没学会啥，san值-2"])
    refreshneed.append([0,0,0,0,0,48,72])
    #75 自习室事件
    evelist.append(eve("../res/image/自习室.png","好朋友邀你去自习室卷卷",2 ,["出发！","不去，在床上摆烂了"] , ["自习了好久，却没学会","摸鱼了但是好不安，应该学习的"]))
    effect.append([[0,0,-2,0,0,12],[0,0,-1,-2,0,4]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["自习了3个小时，却没学会什么 san值-2","摸鱼摸了1个小时，但是不快乐，san值-1，智商-2"])
    refreshneed.append([0,0,0,0,0,32,88])
    #76 舍友想要食品(有负面)
    evelist.append(eve("../res/image/饥渴交加的室友.png","你的舍友饿了，想要一些食物", 2 ,["给他吧","我才不给呢"] , ["给了舍友食物","有什么带来了食物..."]))
    effect.append([[0,0,0,0,0, 2],[0,0,-2,-1,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["给了食物 食物-2","发生矛盾 san值-2 智商-1"])
    refreshneed.append([0,0,0,0,0,48,72])
    #77 舍友想要食品(无负面)
    evelist.append(eve("../res/image/饥渴交加的室友.png","你的舍友饿了，想要一些食物", 2 ,["给他吧","我才不给呢"] , ["给了舍友食物","无事发生"]))
    effect.append([[0,0,0,0,0, 2],[0,0,0,0,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["给了食物 食物-2","无事发生"])
    refreshneed.append([0,0,0,0,0,48,72])
    #78 舍友想要饮品（有负面）
    evelist.append(eve("../res/image/饥渴交加的室友.png","你的舍友渴了，想要一些饮品", 2 ,["给他吧","我才不给呢"] , ["给了舍友饮品","有什么带来了食物..."]))
    effect.append([[0,0,0,0,0, 2],[0,0,0,-2,-1, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])  
    message.append(["给了饮品 饮品-2","发生矛盾 san值-2 智商-1"])
    refreshneed.append([0,0,0,0,0,48,72])
    #79 舍友想要饮品（无负面）
    evelist.append(eve("../res/image/饥渴交加的室友.png","你的舍友渴了，想要一些饮品", 2 ,["给他吧","我才不给呢"] , ["给了舍友饮品","无事发生"]))
    effect.append([[0,0,0,0,0, 2],[0,0,0,0,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["给了饮品 饮品-2","无事发生"])
    refreshneed.append([0,0,0,0,0,48,72])
    #80 上厕所没带纸
    evelist.append(eve("../res/image/一团乱麻.png","在厕所的你没有带纸，你会选择？", 2 ,["试试用口罩？？？","等室友来了向其求救"] , ["不愧是你@~@","等了很久，人麻了"]))
    effect.append([[0,0,-2,0,-2, 4],[-1,-1,-1,0,0, 12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["真亏你能啊 san值-2 清洁-2","饥饿-1 口渴-1 san值-1"])
    refreshneed.append([0,0,0,0,0,72,80])
    #81 口罩用尽（要带）
    evelist.append(eve("../res/image/口罩.png","突然发现没有多的口罩可用", 2 ,["从...里翻个旧的吧","不戴了！"] , ["这...至少防疫意识值得表扬","让你不带口罩！受到批评教育"]))
    effect.append([[0,0,-1,0,-1, 2],[0,0,0,-2,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["有点不太好吧 san值-1 清洁-1","让你不带口罩！ 智商-2"])
    refreshneed.append([0,0,0,0,0,36,52])
    #82 口罩用尽（可不带但带了更好）
    evelist.append(eve("../res/image/口罩.png","突然发现没有多的口罩可用", 2 ,["从...里翻个旧的吧","不戴了！"] , ["突然发现书包里还剩一个","欸嘿，抓不到我"]))
    effect.append([[0,0,+1,0,0, 2],[0,0,0,-2,0, 2]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["运气不错 san值+1","欸嘿，抓不到我"])
    refreshneed.append([0,0,0,0,0,36,52])
    #83 刷单诈骗
    evelist.append(eve("../res/image/刷单.jpg","疫情期间有同学通过网络刷单赚钱", 2 ,["要不也试试","啥玩意儿啊"] , ["谢谢你，大聪明","不理会就好了"]))
    effect.append([[0,0,-1,-2,0, 8],[0,0,0,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["需谨慎 san值-1 智商-2","独自美丽"])
    refreshneed.append([0,0,0,0,0,40,60])
    #84 健康上报（吃）
    evelist.append(eve("../res/image/健康上报.jpg","在床上突然想起还没健康上报", 2 ,["立即赶去上报","算了，明天再说"] , ["无事发生","第二天忘记了，导致没时间吃早餐"]))
    effect.append([[0,0,0,0,0, 8],[-1,0,-1,0,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["无事发生","第二天没吃早餐 san值-1 饥饿-1"])
    refreshneed.append([0,0,0,0,0,84,88])
    #85 健康上报（课）
    evelist.append(eve("../res/image/健康上报.jpg","在床上突然想起还没健康上报", 2 ,["立即赶去上报","算了，明天再说"] , ["无事发生","忘记了，上课迟到了一大截"]))
    effect.append([[0,0,0,0,0, 8],[0,0,0,-2,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]]) 
    message.append(["无事发生","迟到了捏 智商-2"])
    refreshneed.append([0,0,0,0,0,84,88])
    #86 志愿者（负效果）
    evelist.append(eve("../res/image/志愿者.png","芳草社招防疫志愿者咯",2 ,["马上参加","算了算了，还是在寝室睡大觉"] , ["监督防疫时与人发生冲突","听说有志愿者防疫时和人发生冲突，为之难过"]))
    effect.append([[0,0,-2,0,0,20],[0,0,-1,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["防疫工作过程与人冲突，san值-2","心情不好，san值-1"])
    refreshneed.append([0,0,0,0,0,32,60])
    #87 消杀
    evelist.append(eve("../res/image/消杀.jpg","参与校园消杀工作？",2 ,["马上参加","算了算了，还是在寝室睡大觉"] , ["消杀到位","....."]))
    effect.append([[0,0,+1,0,0,20],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["参加防疫工作，san值+1","...."])
    refreshneed.append([0,0,0,0,0,32,60])
    #88 心理咨询
    evelist.append(eve("../res/image/舍友心理问题.jpg","因为被关在学校里，每天想出去玩的舍友抑郁了",2 ,["去开导","我没办法.."] , ["经过友好沟通，你也抑郁了","放着不管好像不好"]))
    effect.append([[0,0,-1,0,0,20],[0,0,-2,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["心情被舍友带跑，san值-1","没有管室友，san值-2"])
    refreshneed.append([0,0,0,0,0,32,60])
    #89 心理咨询2
    evelist.append(eve("../res/image/舍友心理问题.jpg","因为被关在学校里，每天想出去玩的舍友抑郁了",2 ,["找心理委员帮忙","我没办法.."] , ["经过友好沟通，你也抑郁了","放着不管好像不好"]))
    effect.append([[0,0,+1,0,0,20],[0,0,-2,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["室友心情变好了，你很开心，san值+1","没有管室友，san值-2"])
    refreshneed.append([0,0,0,0,0,32,60])
    #90 消毒水和酒精
    evelist.append(eve("../res/image/消毒液.jpg","消毒液用完了",2 ,["找生活委员领取","找安全委员领取"] , ["领到了消毒液","安全委员让你找生活委员QAQ"]))
    effect.append([[0,0,0,0,0,8],[0,0,-1,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["给了消毒液 杂项+2","没有领到消毒液，san值-1"])
    refreshneed.append([0,0,0,0,0,32,80])
    #91 消毒水和酒精2
    evelist.append(eve("../res/image/消毒液.jpg","消毒液用完了",2 ,["找生活委员领取","找安全委员领取"] , ["生活委员让你找安全委员 QAQ","领到了消毒液"]))
    effect.append([[0,0,-1,0,0,8],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["没有领到消毒液，san值-1","给了消毒液 杂项+1"])
    refreshneed.append([0,0,0,0,0,32,80])
    #92 室友借消毒液
    evelist.append(eve("../res/image/室友借消毒液.jpg","室友的消毒液用完了",2 ,["把你的借给他","让他找生活委员领取"] , ["给了室友消毒液，室友给寝室消毒","生活委员的消毒液发完了"]))
    effect.append([[0,0,0,0,+2,8],[0,0,0,0,0,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["给了消毒液，杂项-1，清洁值+2","..."])
    refreshneed.append([0,0,0,0,0,32,80])
    #93 室友借消毒液2
    evelist.append(eve("../res/image/室友借消毒液.jpg","室友的消毒液用完了",2 ,["把你的借给他","让他找安全委员领取"] , ["给了室友消毒液","室友领到了消毒液，还给寝室消了毒"]))
    effect.append([[0,0,0,0,0,8],[0,0,0,0,2,8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["给了消毒液，杂项-1","清洁值+2"])
    refreshneed.append([0,0,0,0,0,32,80])