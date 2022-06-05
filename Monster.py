import pygame
import map1
'''共有4种小怪物，3个普通怪，1个boss'''
# 第一种小怪物
class Monster1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./resource/monsters/1.1.png')
        self.rect = self.image.get_rect()
        self.t = 55  # 已经走过的时间
        self.index = 0  # 目前所在路径列表中的位置
        self.position = 5, 40
        self.rect.left, self.rect.top = self.position
        # 最大生命值
        self.max_life_value = 20
        # 当前生命值
        self.life_value = 20
        # 速度
        self.speed = 10
        # 击杀奖励
        self.reward = 70
        # 对大本营造成的伤害
        self.damage = 1

    def move(self):  # 移动怪物
        self.t += self.speed
        self.rect.left, self.rect.top = map1.get_path(self.t)[0] - 20, map1.get_path(self.t)[1] - 20  # 修改位置

    def die(self):
        global monsters
        monsters = [monster for monster in monsters if monster.t >= 2755]  # 列表中元素的删除方式
        print("monsters的类型是：", type(monsters))
        print(len(monsters))

# 第二种小怪物
class Monster2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./resource/monsters/2.1.png')
        self.rect = self.image.get_rect()
        self.t = 55  # 已经走过的时间
        self.index = 0  # 目前所在路径列表中的位置
        self.position = 60, 40
        self.rect.left, self.rect.top = self.position
        # 最大生命值
        self.max_life_value = 15
        # 当前生命值
        self.life_value = 15
        # 速度
        self.speed = 12
        # 击杀奖励
        self.reward = 70
        # 对大本营造成的伤害
        self.damage = 1

    def move(self):  # 移动怪物
        self.t += self.speed
        self.rect.left, self.rect.top = map1.get_path(self.t)[0] - 20, map1.get_path(self.t)[1] - 20  # 修改位置

    def die(self):
        global monsters
        monsters = [monster for monster in monsters if monster.t >= 2615]  # 列表中元素的删除方式
        print("monsters的类型是：", type(monsters))
        print(len(monsters))
# 第3种小怪物
class Monster3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./resource/monsters/3.1.png')
        self.rect = self.image.get_rect()
        self.t = 55  # 已经走过的时间
        self.index = 0  # 目前所在路径列表中的位置
        self.position = 60, 40
        self.rect.left, self.rect.top = self.position
        # 最大生命值
        self.max_life_value = 40
        # 当前生命值
        self.life_value = 40
        # 速度
        self.speed = 6
        # 击杀奖励
        self.reward = 150
        # 对大本营造成的伤害
        self.damage = 3

    def move(self):  # 移动怪物
        self.t += self.speed
        self.rect.left, self.rect.top = map1.get_path(self.t)[0] - 20, map1.get_path(self.t)[1] - 20  # 修改位置

    def die(self):
        global monsters
        monsters = [monster for monster in monsters if monster.t >= 2615]  # 列表中元素的删除方式
        print("monsters的类型是：", type(monsters))
        print(len(monsters))
# 第4种小怪物
class Monster4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./resource/monsters/4.1.png')
        self.rect = self.image.get_rect()
        self.t = 55  # 已经走过的时间
        self.index = 0  # 目前所在路径列表中的位置
        self.position = 60, 40
        self.rect.left, self.rect.top = self.position
        # 最大生命值
        self.max_life_value = 60
        # 当前生命值
        self.life_value = 60
        # 速度
        self.speed = 4
        # 击杀奖励
        self.reward = 220
        # 对大本营造成的伤害
        self.damage = 5

    def move(self):  # 移动怪物
        self.t += self.speed
        self.rect.left, self.rect.top = map1.get_path(self.t)[0] - 20, map1.get_path(self.t)[1] - 20  # 修改位置

    def die(self):
        global monsters
        monsters = [monster for monster in monsters if monster.t >= 2615]  # 列表中元素的删除方式
        print("monsters的类型是：", type(monsters))
        print(len(monsters))