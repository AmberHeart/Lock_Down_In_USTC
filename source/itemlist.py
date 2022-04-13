import sys
import pygame


class itemlist:  # ! sort分为 0食物 1饮品 2课本 3杂项 4鱼 5 水果  4.5没有种类没有名字不需要加任何东西
    class item:
        def __init__(self, level, name, effect):#稀有度1-4 分别对应红色（常有负面效果） 白色 紫色 金色，名字，作用效果
            self.level = level
            self.name = name
            self.effect = effect
    itemlist = []
    for i in range(0,6):
        itemlist.append([])

    itemlist[0].append(item(1,"老坛酸菜牛肉面","恢复两点饱食度，但是大概率食物中毒"))
    itemlist[0].append(item(1,"双汇火腿肠","恢复一点饱食度，但是小概率食物中毒"))
