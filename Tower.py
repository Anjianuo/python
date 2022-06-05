import pygame
import Bullet
import math
import random
'''炮塔类'''
#法塔
class Tower1(pygame.sprite.Sprite):

	def __init__(self,pos_x,pos_y,shot_angle,cooling_time):
        #shot_angle是射击方向
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./resource/towers/法塔升级1.png')
		self.rect = self.image.get_rect()
		self.cooling_time=cooling_time#箭塔的冷却时间
		self.cooling_now=cooling_time
		self.shot_angle=shot_angle
		self.price=200#箭塔的价格
		self.position = pos_x-50,pos_y-45#这个位置要调
		self.rect.left, self.rect.top = self.position
	'''射击'''
	def shot(self, position):#参数是子弹的位置和角度
		bullet = None
		print(self.cooling_now)

		if self.cooling_now<=0:
			#angle = 2*math.pi*random.randint(0,360)/360#随机生成箭的射击方向
			#bullet=Bullet.bullet1(position[0],position[1],angle)
			#bullets.add(i.shot(i.position))
			self.cooling_now=self.cooling_time
			return 1
		else:
			self.cooling_now-=1
			return 0
#大法塔
class Tower2(pygame.sprite.Sprite):

	def __init__(self,pos_x,pos_y,shot_angle,cooling_time):
        #shot_angle是射击方向
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./resource/towers/法塔升级2.png')
		self.rect = self.image.get_rect()
		self.cooling_time=cooling_time#箭塔的冷却时间
		self.cooling_now=cooling_time
		self.shot_angle=shot_angle
		self.price=300#箭塔的价格
		self.position = pos_x-50,pos_y-45#这个位置要调
		self.rect.left, self.rect.top = self.position
	'''射击'''
	def shot(self, position):#参数是子弹的位置和角度
		bullet = None
		print(self.cooling_now)

		if self.cooling_now<=0:
			#angle = 2*math.pi*random.randint(0,360)/360#随机生成箭的射击方向
			#bullet=Bullet.bullet1(position[0],position[1],angle)
			#bullets.add(i.shot(i.position))
			self.cooling_now=self.cooling_time
			return 1
		else:
			self.cooling_now-=1
			return 0