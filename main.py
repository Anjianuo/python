import numpy as np
import pygame
import Monster
import Tower
import Bullet
import map1
import random
import os
from pygame.locals import*
import sys
from random import*
import math

'''参数设置'''
WIDTH = 1000
HEIGHT = 800
blood_color=(255,0,0)#血条颜色
blood_width=4#血条长度
monster_time=5#怪物出现的频率
my_money=100#初始金币设置为100
home_life_value=20#自己家的生命值
kill = 0 #怪物击杀数量


'''主函数'''
#初始化
pygame.init()
#初始化混音器模块
pygame.mixer.init()
pygame.mixer.music.load("./resource/music/游戏背景1.mp3")
pygame.mixer.music.set_volume(0.3)

hit_sound = pygame.mixer.Sound("./resource/music/hit1.mp3")
hit_sound.set_volume(0.1)

upgrade_sound = pygame.mixer.Sound('./resource/music/箭塔升级.wav')
upgrade_sound.set_volume(0.2)

boss_sound = pygame.mixer.Sound('./resource/music/boss吼叫.mp3')
boss_sound.set_volume(0.2)

in_sound = pygame.mixer.Sound('./resource/music/开门.mp3')
in_sound.set_volume(0.3)

die_sound = pygame.mixer.Sound('./resource/music/小怪物死亡.mp3')
die_sound.set_volume(0.2)

gameover_sound = pygame.mixer.Sound('./resource/music/游戏失败音效.mp3')
gameover_sound.set_volume(0.2)

#创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg=(255,0,0)
background=pygame.image.load('./resource/maps/春天.jpg').convert()#地图
background0=pygame.image.load('./resource/maps/黑色.png').convert()#底色
pygame.display.set_caption("安佳诺：王国保卫战")
clock = pygame.time.Clock()

#用列表存储实例化以后的怪物，子弹，炮塔
monster1=Monster.Monster1()
monsters1 =pygame.sprite.Group(monster1)#建立怪物1的精灵组
monster2=Monster.Monster2()
monster3=Monster.Monster3()
monster4=Monster.Monster4()


tower1=Tower.Tower1(271,426,2,3)
towers1=pygame.sprite.Group(tower1)#建立一个箭塔精灵组

tower2=Tower.Tower2(95,302,2,3)
towers2=pygame.sprite.Group(tower2)#建立一个箭塔精灵组

bullets=pygame.sprite.Group(Bullet.bullet1(271,426,0.78))#建立一个子弹的精灵组
font1 = pygame.font.SysFont('宋体', 30, True)

# 绘制游戏失败界面
gameover1 = pygame.image.load('./resource/maps/黑色.png').convert()
gameover2 = pygame.image.load('./resource/other/gameover.png').convert()

# 游戏结束画面
gameover_font = pygame.font.Font("./font/font.TTF", 48)
again_image = pygame.image.load("./resource/other/again.png").convert_alpha()
again_rect = again_image.get_rect()
gameover_image = pygame.image.load("./resource/other/gameover.png").convert_alpha()
gameover_rect = gameover_image.get_rect()

#关于距离的计算
def cal_dis(x1,y1,x2,y2):
    distance=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    return distance

#实例化怪物移动
def monster1_move():
    for i in monsters1:
        i.move()

#画怪物血条
def draw_blood1():
    for i in monsters1:
        start=(i.rect.left+20,i.rect.top-3)
        end=(i.rect.left+(i.life_value/i.max_life_value)*70+10,i.rect.top-3)
        pygame.draw.line(screen,blood_color,start,end,blood_width)



#碰撞检测,检测是否射中了怪物
def sprite_collide():
    global monsters1
    global monsters2
    global monsters3
    global monsters4
    global bullets
    global attack_power
    global my_money
    global home_life_value
    global kill
    attack_power=3#默认的箭的杀伤力
    dict1=pygame.sprite.groupcollide(monsters1, bullets, False,True, collided=None)

    #确定箭的存在范围
    for i in bullets:
        attack_power=i.attack_power
        if cal_dis(i.position[0],i.position[1],i.begin_pos[0],i.begin_pos[1])>i.scope:
            i.active = False
            bullets.remove(i)
            #hit_sound.play()
        else:
            pass

    for i in dict1:
        i.life_value-=attack_power
        hit_sound.play()


    for i in monsters1:
        if i.life_value<=0:
            die_sound.play()
            kill += 1
            monsters1.remove(i)
            my_money+=i.reward#杀死一个怪物奖励一定的金钱
        elif  i.rect.left > 500 and i.rect.top > 450:
            print("怪物到达了你家")
            home_life_value -= i.damage#对家造成杀伤
            in_sound.play()
            monsters1.remove(i)
        else:
            pass



#显示当前金钱数，箭塔价格，城堡生命值
def draw_text():
    #screen.blit(surface1, [20, 20])
    #screen.blit(my_money,[400,400])
    money = pygame.image.load('./resource/other/金币.png').convert()  # 金币值
    home_life = pygame.image.load('./resource/other/生命.png').convert()  # 生命值
    screen.blit(money,(150,680))
    screen.blit(home_life, (350, 680))
    screen.blit(font1.render(u'%d' % my_money, True, [255, 0, 0]), [250, 710])
    screen.blit(font1.render(u'%d' % home_life_value, True, [255, 0, 0]), [450, 710])
    screen.blit(font1.render(u'kill——%d' % kill, True, [255, 0, 0]), [650, 710])

#子弹的移动
def move_bullet():
    global bullets
    for i in bullets:
        i.move()
        #判断子弹是否超出射程,如果超出范围就删除这个子弹
        if cal_dis(i.position[0],i.position[1],i.begin_pos[0],i.begin_pos[1])>i.scope:
            i.rect.top = -200
            i.rect.left = -200
            #i.active = False
            bullets.remove(i)
        else:
            pass


#箭的射击方向
def shot_bullet():
    for i in towers1:
        k = i.shot(i.position)
        if k:
            # angle = 0
            angle = 2 * math.pi * randint(-90, 90) / 360
            #angle = 2 * math.pi * np.arctan((y1 - y2) / (x1 - x2))  # 随机生成箭的射击方向
            bullets.add(Bullet.bullet1(i.rect.left, i.rect.top, angle))
        else:
            pass
    for i in towers2:
        k = i.shot(i.position)
        if k:
            # angle = 0
            angle = 2 * math.pi * randint(90, 180) / 360
            #angle = 2 * math.pi * np.arctan((y1 - y2) / (x1 - x2))  # 随机生成箭的射击方向
            bullets.add(Bullet.bullet1(i.rect.left, i.rect.top, angle))
        else:
            pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                # 建立一个箭塔，在箭塔精灵组中添加一个箭塔
                if my_money > tower1.price:
                    towers1.add(Tower.Tower1(mouse_x, mouse_y, math.pi, 7))
                    my_money -= tower1.price  # 建立一个箭塔消耗一定的金钱
                else:
                    print("金钱不够")
            if event.key == pygame.K_f:
                # 建立一个箭塔，在箭塔精灵组中添加一个箭塔
                if my_money > tower2.price:
                    towers2.add(Tower.Tower2(mouse_x, mouse_y, math.pi, 7))
                    my_money -= tower2.price  # 建立一个箭塔消耗一定的金钱
                else:
                    print("金钱不够")

#音乐的打断
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()
    else:
        pass
#控制怪物
    if kill < 10:
        if randint(0,100)<monster_time and home_life_value > 0:
            #产生一个怪物
            #boss_sound.play()
            monsters1.add(Monster.Monster1())
        else:
            pass
    elif kill < 20:
        if randint(0,100)<monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster2())
        else:
            pass
    elif kill < 30:
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster3())
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster2())
        else:
            pass
    elif kill < 40:
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster4())
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster3())
        else:
            pass
    elif kill < 45:
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster2())
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster1())
        else:
            pass
    else:
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster4())
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster3())
        if randint(0, 100) < monster_time and home_life_value > 0:
            monsters1.add(Monster.Monster2())
        else:
            pass


    #  绘制游戏结束画面
    if home_life_value <= 0:
        # 背景音乐
        pygame.mixer.music.set_volume(0)
        gameover_sound.play()
        '''screen.blit(gameover1,(0,0))
        screen.blit(gameover2, (350, 400))
        gameover_rect.left, gameover_rect.top = 350,400
        gameover_rect.right, gameover_rect.bottom = 650, 441

        # 检测用户的鼠标操作
        # 如果用户按下鼠标左键
        if pygame.mouse.get_pressed()[0]:
            # 获取鼠标坐标
            pos = pygame.mouse.get_pos()
            # 如果用户点击“结束游戏”
            if gameover_rect.left < pos[0] < gameover_rect.right and \
                    gameover_rect.top < pos[1] < gameover_rect.bottom:
                # 退出游戏
                pygame.quit()
                sys.exit()
            else:
                pass'''


    monster1_move()  # 移动怪物

    shot_bullet()  # 射箭
    sprite_collide()
    move_bullet()
    monsters1.update()

    towers1.update()
    towers2.update()
    bullets.update()

    screen.blit(background0, (0, 0))
    screen.blit(background, (0, 0))
    draw_blood1()
    draw_text()
    monsters1.draw(screen)

    towers1.draw(screen)
    towers2.draw(screen)
    bullets.draw(screen)

    clock.tick(4)
    pygame.display.update()