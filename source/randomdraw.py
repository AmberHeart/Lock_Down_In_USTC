import sys
import pygame


class Randdraw:
    
    def spawn_item():
        judge_num = random.randint(0,99)
        if 95 <= judge_num:
            #legendary
            return 1
        elif 80 <= judge_num:
            #epic
            return 2
        elif 50 <= judge_num:
            #rare
            return 3
        else:
            #common
            return 4
        
    def getdraw(start_item):

        draw_result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0],[0]]

        for i in range(0,4):
            for j in range(0,start_item[i]):
                draw_result[i][spawn_item()] += 1
                
        return draw_result
