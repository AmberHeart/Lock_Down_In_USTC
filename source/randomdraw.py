import sys
import pygame

class Randdraw:

    l_item_num = [1,1,1,1,1,1]
    e_item_num = [1,1,1,1,1,1]
    r_item_num = [1,1,1,1,1,1]
    c_item_num = [1,1,1,1,1,1]
    l_no = [[1],[2],[3],[4],[5],[6]]
    e_no = [[7],[8],[9],[10],[11],[12]]
    r_no = [[13],[14],[15],[16],[17],[18]]
    c_no = [[19],[20],[21],[22],[23],[24]]
    
    def spawn_item(kind):
        judge_num = random.randint(0,99)
        if 95 <= judge_num:
            #legendary
            j_n = random.randint(0,l_item_num[kind]) + 1
            return l_no[kind][j_n]
        elif 80 <= judge_num:
            #epic
            j_n = random.randint(0,e_item_num[kind]) + 1
            return e_no[kind][j_n]
        elif 50 <= judge_num:
            #rare
            j_n = random.randint(0,r_item_num[kind]) + 1
            return r_no[kind][j_n]
        else:
            #common
            j_n = random.randint(0,c_item_num[kind]) + 1
            return c_no[kind][j_n]
        
    def getdraw(start_item):

        draw_result = []

        for i in range(0,6):
            draw_result.append([])
            for i in range(0,start_item[i]):
                draw_result[i].append(spawn_item(i))
                
        return draw_result
